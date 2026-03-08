"""change_team_logo_url_to_text

Revision ID: 4a1b715e70cb
Revises: 47529fc5cadf
Create Date: 2026-03-08 09:10:57.270086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a1b715e70cb'
down_revision: Union[str, None] = '47529fc5cadf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Change logo_url column from VARCHAR(500) to TEXT to support base64 encoded images
    op.alter_column('teams', 'logo_url',
                    existing_type=sa.String(500),
                    type_=sa.Text(),
                    existing_nullable=True)


def downgrade() -> None:
    # Revert logo_url column back to VARCHAR(500)
    op.alter_column('teams', 'logo_url',
                    existing_type=sa.Text(),
                    type_=sa.String(500),
                    existing_nullable=True)
