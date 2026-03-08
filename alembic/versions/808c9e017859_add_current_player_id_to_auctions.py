"""add_current_player_id_to_auctions

Revision ID: 808c9e017859
Revises: 4a1b715e70cb
Create Date: 2026-03-08 17:58:24.984451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '808c9e017859'
down_revision: Union[str, None] = '4a1b715e70cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add current_player_id column to auctions table
    op.add_column('auctions', sa.Column('current_player_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_auctions_current_player_id'), 'auctions', ['current_player_id'], unique=False)
    op.create_foreign_key(
        'fk_auctions_current_player_id_players',
        'auctions', 'players',
        ['current_player_id'], ['id'],
        ondelete='SET NULL'
    )


def downgrade() -> None:
    # Remove current_player_id column from auctions table
    op.drop_constraint('fk_auctions_current_player_id_players', 'auctions', type_='foreignkey')
    op.drop_index(op.f('ix_auctions_current_player_id'), table_name='auctions')
    op.drop_column('auctions', 'current_player_id')
