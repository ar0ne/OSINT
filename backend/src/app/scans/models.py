from datetime import datetime
from typing import List, Optional

from pydantic import validator
from sqlalchemy import Column, Integer, String

from app.database.core import Base
from app.models import AppBaseModel, Pagination, PrimaryKey, TimeStampMixin

from .enums import ScanStatus


class Scan(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    status = Column(String, default=ScanStatus.created, nullable=False)
    data = Column(String, nullable=True)
    domain = Column(String, nullable=False)
    tool = Column(String, nullable=False)


class ScanRead(AppBaseModel):
    id: PrimaryKey
    status: Optional[str]
    data: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ScanReadMinimal(AppBaseModel):
    id: PrimaryKey
    status: str
    created_at: Optional[datetime]


class ScanPagination(Pagination):
    items: List[ScanReadMinimal]


class ScanCreate(AppBaseModel):
    domain: str
    tool: str

    @validator("domain")
    def domain_required(cls, v):
        if not v:
            raise ValueError("must not be empty string")
