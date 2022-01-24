"""add foreign-key to posts table

Revision ID: 064f254e2720
Revises: 7a22071b580a
Create Date: 2022-01-24 16:19:01.411799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '064f254e2720'
down_revision = '7a22071b580a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE") # remot_cols is for id from users

    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    
    pass
