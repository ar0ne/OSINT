"""create tool table

Revision ID: 7dabf177979b
Revises: 1488d6822447
Create Date: 2024-09-13 14:19:55.675473

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '7dabf177979b'
down_revision: Union[str, None] = '1488d6822447'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tool",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False, unique=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )
    op.add_column("scan", sa.Column(
        "tool_id",
        sa.Integer,
        sa.ForeignKey("tool.id", ondelete='SET NULL'), nullable=True)
    )
    op.drop_column("scan", "tool")


def downgrade() -> None:
    op.drop_column("scan", "tool_id")
    op.drop_table("tool")
    op.add_column(
        'scan', sa.Column('tool', sa.String(length=25), nullable=True))
