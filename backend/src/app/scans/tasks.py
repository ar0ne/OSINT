import logging

from sqlalchemy.orm import Session

from app.tasks import celery

from .models import Scan

log = logging.getLogger(__name__)


@celery.task(name="schedule_scan")
def schedule_scan(
    *, scan_id: str, db_session: Session | None = None
) -> int:
    """Complete a scan"""
    log.info("Scan scheduler")

    import time
    time.sleep(2)

    return 2/0
