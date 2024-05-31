"""empty message

Revision ID: 532bb7597315
Revises: 11e5949352b6
Create Date: 2024-05-29 11:41:02.796767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '532bb7597315'
down_revision = '11e5949352b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resumes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('my_skill', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resumes', schema=None) as batch_op:
        batch_op.drop_column('my_skill')

    # ### end Alembic commands ###