"""empty message

Revision ID: 513bc8f9c3e6
Revises: 62c5b3fe3e84
Create Date: 2020-02-15 17:21:33.955073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '513bc8f9c3e6'
down_revision = '62c5b3fe3e84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue_desc', sa.String(length=255), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Artist', 'seeking_venue_desc')
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
