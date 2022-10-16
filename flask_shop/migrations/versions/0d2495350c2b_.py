"""empty message

Revision ID: 0d2495350c2b
Revises: cd11497d9c0e
Create Date: 2022-10-15 11:44:57.067447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0d2495350c2b'
down_revision = 'cd11497d9c0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_role_permission', sa.Column('pid', sa.Integer(), nullable=True))
    op.drop_constraint('t_role_permission_ibfk_1', 't_role_permission', type_='foreignkey')
    op.create_foreign_key(None, 't_role_permission', 't_permission', ['pid'], ['id'])
    op.drop_column('t_role_permission', 'mid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_role_permission', sa.Column('mid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 't_role_permission', type_='foreignkey')
    op.create_foreign_key('t_role_permission_ibfk_1', 't_role_permission', 't_permission', ['mid'], ['id'])
    op.drop_column('t_role_permission', 'pid')
    # ### end Alembic commands ###