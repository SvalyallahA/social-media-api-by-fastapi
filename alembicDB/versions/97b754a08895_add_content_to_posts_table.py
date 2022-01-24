"""add content to posts table

Revision ID: 97b754a08895
Revises: b3d9156427f5
Create Date: 2022-01-24 15:45:25.786216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97b754a08895'
down_revision = 'b3d9156427f5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
