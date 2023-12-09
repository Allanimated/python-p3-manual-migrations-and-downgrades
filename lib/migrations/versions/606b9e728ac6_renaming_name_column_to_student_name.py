"""Renaming name column to student_name

Revision ID: 606b9e728ac6
Revises: 54f37caf957d
Create Date: 2023-12-09 15:04:18.452755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '606b9e728ac6'
down_revision = '54f37caf957d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("scholars", "name", new_column_name = "student_name")


def downgrade() -> None:
    op.alter_column("scholars", "student_name", new_column_name = "name")
