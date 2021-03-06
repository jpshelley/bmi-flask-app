"""empty message

Revision ID: 39b978afef3a
Revises: 2ea18a507d65
Create Date: 2015-04-11 21:35:28.188436

"""

# revision identifiers, used by Alembic.
revision = '39b978afef3a'
down_revision = '2ea18a507d65'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('height', sa.Integer(), nullable=True))
    op.add_column('results', sa.Column('weight', sa.Integer(), nullable=True))
    op.drop_column('results', 'url')
    op.drop_column('results', 'result_all')
    op.drop_column('results', 'result_no_stop_words')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('result_no_stop_words', postgresql.JSON(), autoincrement=False, nullable=True))
    op.add_column('results', sa.Column('result_all', postgresql.JSON(), autoincrement=False, nullable=True))
    op.add_column('results', sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('results', 'weight')
    op.drop_column('results', 'height')
    ### end Alembic commands ###
