"""empty message

Revision ID: 3370c2c84c21
Revises: 748bd3062da2
Create Date: 2022-10-17 16:44:30.428546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3370c2c84c21'
down_revision = '748bd3062da2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_article', sa.Column('cover', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_article', 'cover')
    # ### end Alembic commands ###