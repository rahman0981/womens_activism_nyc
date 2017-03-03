"""updated Modules table

Revision ID: d18570d16a30
Revises: 243d0f8552d8
Create Date: 2017-03-03 18:04:10.315219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd18570d16a30'
down_revision = '243d0f8552d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modules', sa.Column('is_active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('modules', 'is_active')
    # ### end Alembic commands ###
