"""Initial Migration - Joel Castillo

Revision ID: 8bf06a4b6b5c
Revises: None
Create Date: 2016-08-18 00:58:12.917615

"""

# revision identifiers, used by Alembic.
revision = '8bf06a4b6b5c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('reason', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('passwords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('p1', sa.String(length=128), nullable=True),
    sa.Column('p2', sa.String(length=128), nullable=True),
    sa.Column('p3', sa.String(length=128), nullable=True),
    sa.Column('p4', sa.String(length=128), nullable=True),
    sa.Column('p5', sa.String(length=128), nullable=True),
    sa.Column('last_changed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('site', sa.String(length=50), nullable=True),
    sa.Column('is_subscribed', sa.Boolean(), nullable=True),
    sa.Column('login_attempts', sa.Integer(), nullable=True),
    sa.Column('old_passwords', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['old_passwords'], ['passwords.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_table('stories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activist_first', sa.String(length=30), nullable=True),
    sa.Column('activist_last', sa.String(length=30), nullable=True),
    sa.Column('activist_start', sa.String(length=4), nullable=True),
    sa.Column('activist_end', sa.String(length=5), nullable=True),
    sa.Column('activist_url', sa.Text(), nullable=True),
    sa.Column('poster_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('creation_time', sa.DateTime(), nullable=False),
    sa.Column('edit_time', sa.DateTime(), nullable=True),
    sa.Column('is_edited', sa.Boolean(), nullable=False),
    sa.Column('is_visible', sa.Boolean(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('image_link', sa.Text(), nullable=True),
    sa.Column('video_link', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['poster_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('story_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=30), nullable=True),
    sa.Column('reason', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['story_id'], ['stories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('story_edits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('story_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('creation_time', sa.DateTime(), nullable=True),
    sa.Column('edit_time', sa.DateTime(), nullable=True),
    sa.Column('type', sa.String(length=6), nullable=False),
    sa.Column('activist_first', sa.String(length=30), nullable=True),
    sa.Column('activist_last', sa.String(length=30), nullable=True),
    sa.Column('activist_start', sa.String(length=4), nullable=True),
    sa.Column('activist_end', sa.String(length=5), nullable=True),
    sa.Column('activist_url', sa.Text(), nullable=True),
    sa.Column('poster_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('reason', sa.Text(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('image_link', sa.Text(), nullable=True),
    sa.Column('video_link', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['poster_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['story_id'], ['stories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('story_tags',
    sa.Column('story_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['story_id'], ['stories.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('story_id', 'tag_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('story_tags')
    op.drop_table('story_edits')
    op.drop_table('flags')
    op.drop_table('stories')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    op.drop_table('passwords')
    op.drop_table('feedback')
    ### end Alembic commands ###
