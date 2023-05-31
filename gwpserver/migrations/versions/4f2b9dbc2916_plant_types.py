"""plant types

Revision ID: 4f2b9dbc2916
Revises: 3ee7c5a1c4bb
Create Date: 2023-05-25 09:39:25.749674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f2b9dbc2916'
down_revision = '3ee7c5a1c4bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planttypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plant_type', sa.Integer(), nullable=True),
    sa.Column('min_moisture', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planttypes')
    # ### end Alembic commands ###
