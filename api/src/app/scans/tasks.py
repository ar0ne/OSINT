import logging
from typing import Dict, Tuple

from app.database.core import get_session
from app.tasks import celery

from .models import ScanStatus, ScanUpdate
from .service import get, update

log = logging.getLogger(__name__)


def get_data_from_external_api(scan_id: str) -> Tuple[Dict[str, str], bool]:
    log.info("Call external API")
    # simulate external API call
    import random
    import time

    # block on IO
    time.sleep(5)

    response = {
        "data": f"Some text data: {random.randint(0, 1000)}"
    }
    status = bool(random.getrandbits(1))
    return response, status


@celery.task(name="schedule_scan")
def schedule_scan(*, scan_id: str) -> bool:
    """Complete a scan"""
    log.info("Scan scheduler")

    with get_session() as db_session:
        scan = get(db_session=db_session, scan_id=scan_id)
        scan = update(db_session=db_session, scan=scan, scan_in=ScanUpdate(
            data=None, status=ScanStatus.in_progress))

    response, success = get_data_from_external_api(scan_id)

    scan_in = ScanUpdate(
        data=response["data"],
        status=ScanStatus.succeeded if success else ScanStatus.failed
    )

    with get_session() as db_session:
        scan = update(db_session=db_session, scan=scan, scan_in=scan_in)

    return success
