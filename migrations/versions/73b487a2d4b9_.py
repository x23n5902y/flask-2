"""empty message

Revision ID: 73b487a2d4b9
Revises: f8fe40b594f6
Create Date: 2021-12-15 06:14:43.439252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73b487a2d4b9'
down_revision = 'f8fe40b594f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('role', sa.String(length=32), server_default='simple_user', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_model', 'role')
    # ### end Alembic commands ###
