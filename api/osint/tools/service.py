from typing import List

from osint.database.core import DbSession

from .models import Tool


def get_all(*, db_session: DbSession) -> List[Tool]:
    return db_session.query(Tool).all()


def get(*, db_session: DbSession, tool_id: int) -> Tool:
    return db_session.query(Tool).filter(Tool.id == tool_id).first()
