from typing import List

from osint.database.core import DbSession

from .models import Tool


def get_all(*, db_session: DbSession) -> List[Tool]:
    return db_session.query(Tool).all()
