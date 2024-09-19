import logging
from typing import Tuple

from osint import config
from osint.database.core import get_session
from osint.tasks import celery
from osint.tools.clients import DataClientFactory

from .models import ScanStatus, ScanUpdate
from .service import get, get_last_x_hours_by_domain, update

log = logging.getLogger(__name__)


def get_data_from_external_api(tool: str, domain: str) -> Tuple[str | None, bool]:
    log.info(f"Call {tool} API")
    client = DataClientFactory.get_client(tool)
    try:
        data = client.get_data(domain)
        return data, True
    except Exception as err:
        # ignore any errors and hide them from user
        log.warning(err)
    return None, False


@celery.task(name="schedule_scan")
def schedule_scan(*, scan_id: str) -> bool:
    """Complete a scan"""
    log.info(f"Start scanning for {scan_id=}")

    with get_session() as db_session:
        scan = get(db_session=db_session, scan_id=scan_id)
        scan = update(db_session=db_session, scan=scan, scan_in=ScanUpdate(
            data=None, status=ScanStatus.in_progress))
        domain = scan.domain
        if (existing_scan := get_last_x_hours_by_domain(
            db_session=db_session, domain=domain, hours=config.SCAN_RESULT_ACTUAL_TIME
        )):
            log.info(f"Found recent scan result for the {domain=}")
            scan = update(
                db_session=db_session,
                scan=scan,
                scan_in=ScanUpdate(data=existing_scan.data, status=existing_scan.status)
            )
            return True
        tool_name = scan.tool.name

    data, success = get_data_from_external_api(tool_name, domain)

    scan_in = ScanUpdate(
        data=data,
        status=ScanStatus.succeeded if success else ScanStatus.failed
    )

    with get_session() as db_session:
        scan = update(db_session=db_session, scan=scan, scan_in=scan_in)

    log.info(f"Finished scanning for {domain} with {tool_name}")
    return success
