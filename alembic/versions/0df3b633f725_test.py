"""test

Revision ID: 0df3b633f725
Revises: 95cce87fe4c2
Create Date: 2025-01-30 14:06:35.069768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0df3b633f725'
down_revision: Union[str, None] = '95cce87fe4c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('subscription_model', sa.Enum('FREE', 'PLUS', 'PREMUIM', name='costomersubmodel'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('wallet_money_amount', sa.Float(), nullable=False),
    sa.Column('subscription_end_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('authors_user_id_fkey', 'authors', type_='foreignkey')
    op.drop_constraint('authors_city_id_fkey', 'authors', type_='foreignkey')
    op.create_foreign_key(None, 'authors', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'authors', 'cities', ['city_id'], ['id'], ondelete='CASCADE')
    op.alter_column('books', 'genre_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('books_genre_id_fkey', 'books', type_='foreignkey')
    op.create_foreign_key(None, 'books', 'genres', ['genre_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.create_foreign_key('books_genre_id_fkey', 'books', 'genres', ['genre_id'], ['id'])
    op.alter_column('books', 'genre_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'authors', type_='foreignkey')
    op.drop_constraint(None, 'authors', type_='foreignkey')
    op.create_foreign_key('authors_city_id_fkey', 'authors', 'cities', ['city_id'], ['id'])
    op.create_foreign_key('authors_user_id_fkey', 'authors', 'users', ['user_id'], ['id'])
    op.drop_table('customers')
    # ### end Alembic commands ###
