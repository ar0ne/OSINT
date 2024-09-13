from typing import List

from sqlalchemy import Column, Integer, String

from osint.database.core import Base
from osint.models import OsintBaseModel, PrimaryKey, TimeStampMixin


class Tool(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class ToolRead(OsintBaseModel):
    id: PrimaryKey
    name: str


class ToolsRead(OsintBaseModel):
    data: List[ToolRead]
