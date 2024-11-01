"""Renaming students to scholars

Revision ID: afa3f1cde8a1
Revises: 791279dd0760
Create Date: 2024-10-31 22:25:15.036202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afa3f1cde8a1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
