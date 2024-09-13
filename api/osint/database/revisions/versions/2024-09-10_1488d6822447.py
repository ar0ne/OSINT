"""updated scans table

Revision ID: 1488d6822447
Revises: 4aba7c8a2a41
Create Date: 2024-09-10 18:23:24.747825

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1488d6822447'
down_revision: Union[str, None] = '4aba7c8a2a41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('scan', sa.Column('domain', sa.String, nullable=False))
    op.add_column(
        'scan', sa.Column('tool', sa.String(length=25), nullable=False))


def downgrade() -> None:
    op.drop_column("scan", "domain")
    op.drop_column("scan", "tool")
