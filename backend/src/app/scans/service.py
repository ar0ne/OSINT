from typing import Optional

from sqlalchemy_filters import apply_pagination

from app import config

from .models import Scan, ScanCreate, ScanPagination


def get(*, db_session, scan_id: int) -> Optional[Scan]:
    """Returns a scan based on the given id."""
    return db_session.query(Scan).filter(Scan.id == scan_id).first()


def get_paginated(*, db_session, page: int | None, items_per_page: int | None) -> ScanPagination:
    """returns page of scans"""
    query = db_session.query(Scan)
    if not page:
        page = 1
    if not items_per_page:
        items_per_page = config.PAGINATION_PAGE_SIZE

    paginated_query, pagination = apply_pagination(query, page_number=page, page_size=items_per_page)

    return {
        "items": paginated_query.all(),
        "count": pagination.page_size,
        "page": pagination.page_number,
        "total": pagination.total_results,
    }


def create(*, db_session, scan_in: ScanCreate) -> Scan:
    """Create a new scan"""
    scan = Scan(
    )

    db_session.add(scan)
    db_session.commit()

    return scan
