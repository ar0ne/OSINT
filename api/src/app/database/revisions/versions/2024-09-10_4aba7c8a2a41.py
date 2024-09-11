"""create scans table

Revision ID: 4aba7c8a2a41
Revises: 5fb668e32ac1
Create Date: 2024-09-10 11:22:41.403965

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4aba7c8a2a41"
down_revision: Union[str, None] = "5fb668e32ac1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "scan",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("data", sa.Text),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("status", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("scan")
