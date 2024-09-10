import logging

from sqlalchemy.orm import Session

from app.decorators import background_task

from .models import Scan

log = logging.getLogger(__name__)


@background_task
def schedule_scan(
    *, scan_id: str, db_session: Session | None = None
) -> Scan:
    """Complete a scan"""
    log.info("Scan scheduler")
