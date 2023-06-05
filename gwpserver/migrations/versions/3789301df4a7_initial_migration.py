"""initial migration

Revision ID: 3789301df4a7
Revises: 
Create Date: 2023-04-21 10:36:35.882533

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3789301df4a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_column('lastWatered')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastWatered', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###