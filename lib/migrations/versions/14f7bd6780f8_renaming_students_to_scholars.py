"""Renaming students to scholars

Revision ID: 14f7bd6780f8
Revises: afa3f1cde8a1
Create Date: 2024-10-31 22:31:49.011739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14f7bd6780f8'
down_revision = 'afa3f1cde8a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
