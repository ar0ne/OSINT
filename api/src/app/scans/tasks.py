import logging
from typing import Dict, List, Tuple

import requests

from app.database.core import get_session
from app.tasks import celery

from .models import Scan, ScanStatus, ScanUpdate
from .service import get, update

log = logging.getLogger(__name__)


THE_HARVESTER_URL = "http://0.0.0.0:8083"


def get_sources(tool: str) -> List[str]:
    # TODO: not the best idea, since some sources require API key
    try:
        sources = requests.get(f"{THE_HARVESTER_URL}/sources").json()["sources"]
        return ",".join(sources)

    except requests.exceptions.RequestException:
        pass
    return []


def get_data_from_external_api(tool: str, domain: str) -> Tuple[str, bool]:
    log.info("Call external API")
    try:
        sources = get_sources(tool)

        resp = requests.get(f"{THE_HARVESTER_URL}/query/?domain={domain}&source={sources}")
        resp.raise_for_status()
        return resp.content, True
    except Exception as err:
        log.warning(err)
    return "", False


@celery.task(name="schedule_scan")
def schedule_scan(*, scan_id: str) -> bool:
    """Complete a scan"""
    log.info("Scan scheduler")

    with get_session() as db_session:
        scan = get(db_session=db_session, scan_id=scan_id)
        scan = update(db_session=db_session, scan=scan, scan_in=ScanUpdate(
            data=None, status=ScanStatus.in_progress))
        domain, tool = scan.domain, scan.tool

    data, success = get_data_from_external_api(tool, domain)

    scan_in = ScanUpdate(
        data=data,
        status=ScanStatus.succeeded if success else ScanStatus.failed
    )

    with get_session() as db_session:
        scan = update(db_session=db_session, scan=scan, scan_in=scan_in)

    log.info(f"Finished scanning for {domain} with {tool}")
    return success
