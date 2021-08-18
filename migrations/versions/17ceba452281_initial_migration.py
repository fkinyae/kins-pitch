"""Initial Migration

Revision ID: 17ceba452281
Revises: 3a978a39f7c1
Create Date: 2021-08-18 12:21:31.887072

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '17ceba452281'
down_revision = '3a978a39f7c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('categories_user_id_fkey', 'categories', type_='foreignkey')
    op.drop_column('categories', 'posted')
    op.drop_column('categories', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('categories', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_foreign_key('categories_user_id_fkey', 'categories', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
