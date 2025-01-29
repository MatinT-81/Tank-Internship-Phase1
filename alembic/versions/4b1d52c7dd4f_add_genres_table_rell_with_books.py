"""add genres table + rell with books

Revision ID: 4b1d52c7dd4f
Revises: bff91a604913
Create Date: 2025-01-29 09:11:08.880698

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '4b1d52c7dd4f'
down_revision: Union[str, None] = 'bff91a604913'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('genre_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'books', 'genres', ['genre_id'], ['id'])
    op.drop_column('books', 'genre')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('genre', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'genre_id')
    op.drop_table('genres')
    # ### end Alembic commands ###
