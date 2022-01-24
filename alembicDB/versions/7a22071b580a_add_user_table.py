"""add user table

Revision ID: 7a22071b580a
Revises: 97b754a08895
Create Date: 2022-01-24 15:55:54.877606

"""
import email
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a22071b580a'
down_revision = '97b754a08895'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
