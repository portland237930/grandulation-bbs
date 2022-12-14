"""empty message

Revision ID: 5397a8c53892
Revises: 4baad1f32e85
Create Date: 2022-10-25 20:24:39.375272

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5397a8c53892'
down_revision = '4baad1f32e85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_wxuser')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_wxuser',
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('update_time', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nick_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('wxuser', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('avatar_url', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['wxuser'], ['t_wxuser.id'], name='t_wxuser_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
