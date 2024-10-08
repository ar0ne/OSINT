from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy_filters import apply_pagination

from osint import config
from osint.database.core import DbSession

from .models import Scan, ScanCreate, ScanPagination, ScanStatus, ScanUpdate


def get(*, db_session, scan_id: int) -> Optional[Scan]:
    """Returns a scan based on the given id."""
    return db_session.query(Scan).filter(Scan.id == scan_id).first()


def get_last_x_hours_by_domain(
    *, db_session: DbSession, domain: str, hours: int
) -> Optional[Scan]:
    """Returns a scan for domain"""
    now = datetime.utcnow()
    return (
        db_session.query(Scan)
        .filter(Scan.domain == domain)
        .filter(Scan.status == ScanStatus.succeeded)
        .filter(Scan.updated_at >= now - timedelta(hours=hours))
        .first()
    )


def get_paginated(
    *, db_session, page: int | None, items_per_page: int | None
) -> ScanPagination:
    """returns page of scans"""
    query = db_session.query(Scan)
    query = query.order_by(Scan.created_at.desc())
    if not page:
        page = 1
    if not items_per_page:
        items_per_page = config.PAGINATION_PAGE_SIZE

    paginated_query, pagination = apply_pagination(
        query, page_number=page, page_size=items_per_page)

    return {
        "items": paginated_query.all(),
        "count": pagination.page_size,
        "page": pagination.page_number,
        "total": pagination.total_results,
    }


def create(*, db_session: DbSession, scan_in: ScanCreate) -> Scan:
    """Create a new scan"""
    scan = Scan(
        domain=scan_in.domain,
        tool_id=scan_in.tool_id,
        status=ScanStatus.new,
    )

    db_session.add(scan)
    db_session.commit()

    return scan


def update(*, db_session: DbSession, scan: Scan, scan_in: ScanUpdate) -> Scan:

    scan.data = scan_in.data
    scan.status = scan_in.status

    db_session.add(scan)
    db_session.commit()

    return scan
