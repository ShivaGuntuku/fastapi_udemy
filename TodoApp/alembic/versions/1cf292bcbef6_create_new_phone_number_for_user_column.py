"""Create new phone number for user column

Revision ID: 1cf292bcbef6
Revises: 63dc84e3113c
Create Date: 2024-02-07 14:59:05.905842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cf292bcbef6'
down_revision: Union[str, None] = '63dc84e3113c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
