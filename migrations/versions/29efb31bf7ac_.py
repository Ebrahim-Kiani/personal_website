"""empty message

Revision ID: 29efb31bf7ac
Revises: 0835db963625
Create Date: 2024-05-31 17:16:37.547086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29efb31bf7ac'
down_revision = '0835db963625'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
