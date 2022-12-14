"""empty message

Revision ID: 4baad1f32e85
Revises: 
Create Date: 2022-10-25 20:04:07.419648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4baad1f32e85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_wxuser',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nick_name', sa.String(length=255), nullable=True),
    sa.Column('wxuser', sa.Integer(), nullable=True),
    sa.Column('avatar_url', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['wxuser'], ['t_wxuser.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'comments', 't_user', ['uid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_table('t_wxuser')
    # ### end Alembic commands ###
