"""Add Machine model

Revision ID: 811eb9ba72c0
Revises: 36fc3c874c38
Create Date: 2024-05-24 13:33:10.504694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '811eb9ba72c0'
down_revision = '36fc3c874c38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('machine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('price_per_day', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('machine')
    # ### end Alembic commands ###
