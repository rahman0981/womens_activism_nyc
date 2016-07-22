"""empty message

Revision ID: eae09133ab90
Revises: 111099650c83
Create Date: 2016-07-22 10:15:51.237637

"""

# revision identifiers, used by Alembic.
revision = 'eae09133ab90'
down_revision = '111099650c83'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment_edits', 'type',
               existing_type=sa.VARCHAR(length=6),
               nullable=False)
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('comment_edits', 'type',
               existing_type=sa.VARCHAR(length=6),
               nullable=True)
    ### end Alembic commands ###
