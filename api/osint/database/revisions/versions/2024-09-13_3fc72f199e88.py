"""add theHarvester tool

Revision ID: 3fc72f199e88
Revises: 7dabf177979b
Create Date: 2024-09-13 14:26:48.310846

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision: str = '3fc72f199e88'
down_revision: Union[str, None] = '7dabf177979b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(text("insert into tool (name) values ('theHarvester')"))


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(text("delete from tool where name = 'theHarvester'"))
