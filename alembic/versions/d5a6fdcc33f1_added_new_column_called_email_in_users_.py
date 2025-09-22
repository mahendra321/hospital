"""added new column called email in users table

Revision ID: d5a6fdcc33f1
Revises: e628a215708c
Create Date: 2025-09-19 17:58:09.073498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5a6fdcc33f1'
down_revision: Union[str, Sequence[str], None] = 'e628a215708c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users",sa.Column("email",sa.String() ,nullable=False))

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users",sa.Column("email",sa.String() ,nullable=False))
