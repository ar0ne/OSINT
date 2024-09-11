import logging

from fastapi import APIRouter, HTTPException, status

from app.database.core import DbSession
from app.models import PrimaryKey

from .models import ScanCreate, ScanPagination, ScanRead
from .service import create, get, get_paginated
from .tasks import schedule_scan

log = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "",
    response_model=ScanPagination,
    summary="Retrieve a list of scans.",
)
def get_scans(
    db_session: DbSession,
    page: int | None = None,
    page_size: int | None = None,
):
    """Retrieves a list of scans."""
    return get_paginated(db_session=db_session, page=page, items_per_page=page_size)


@router.get(
    "/{scan_id}",
    response_model=ScanRead,
    summary="Retrieves a single scan."
)
def get_scan(
    scan_id: PrimaryKey,
    db_session: DbSession,
):
    scan = get(db_session=db_session, scan_id=scan_id)

    if not scan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Scan with this ID not found."}]
        )
    return scan


@router.post(
    "",
    response_model=ScanRead,
    summary="Creates a new scan",
)
def create_scan(
    db_session: DbSession,
    scan_in: ScanCreate,
    
):
    """Creates new scan"""
    scan = create(db_session=db_session, scan_in=scan_in)
    schedule_scan.delay(scan_id=scan.id)
    return scan
