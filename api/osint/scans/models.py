from datetime import datetime
from typing import List, Optional

from pydantic import validator
from sqlalchemy import Column, ForeignKey, Integer, String
from validators.domain import domain

from osint.database.core import Base
from osint.models import OsintBaseModel, Pagination, PrimaryKey, TimeStampMixin

from .enums import ScanStatus


class Scan(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    status = Column(String, default=ScanStatus.new, nullable=False)
    data = Column(String, nullable=True)
    domain = Column(String, nullable=False)
    tool_id = Column(Integer, ForeignKey("tool.id"), nullable=True)


class ScanRead(OsintBaseModel):
    id: PrimaryKey
    status: str
    data: Optional[str]
    domain: str
    tool: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ScanReadMinimal(OsintBaseModel):
    id: PrimaryKey
    status: str
    domain: str
    tool: str
    created_at: Optional[datetime]


class ScanPagination(Pagination):
    items: List[ScanReadMinimal]


class ScanCreate(OsintBaseModel):
    domain: str
    tool: str

    @validator("domain")
    def domain_required(cls, v):
        if not v:
            raise ValueError("must not be empty string")
        if domain(v) is not True:
            raise ValueError("invalid domain")
        return v


class ScanUpdate(OsintBaseModel):
    data: Optional[str]
    status: str
