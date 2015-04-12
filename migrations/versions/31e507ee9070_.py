"""empty message

Revision ID: 31e507ee9070
Revises: 39b978afef3a
Create Date: 2015-04-11 22:16:40.402297

"""

# revision identifiers, used by Alembic.
revision = '31e507ee9070'
down_revision = '39b978afef3a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('bmi', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'bmi')
    ### end Alembic commands ###
