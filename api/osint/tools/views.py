import logging

from fastapi import APIRouter

from osint.database.core import DbSession

from .models import ToolsRead
from .service import get_all

log = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "",
    response_model=ToolsRead,
    summary="Retrieve a list of available tools"
)
def get_tools(
    db_session: DbSession
):
    """Retrieve a list of tools"""
    tools = get_all(db_session=db_session)
    return {"data": tools}
