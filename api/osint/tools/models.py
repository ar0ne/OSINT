from sqlalchemy import Column, Integer, String

from osint.database.core import Base
from osint.models import TimeStampMixin


class Tool(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
