"""empty message

Revision ID: 33ee434d14e3
Revises: 2810ce26144c
Create Date: 2024-05-23 22:38:43.328647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33ee434d14e3'
down_revision = '2810ce26144c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('awards', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('Complete_Projects', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('Happy_Customers', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('Cups_of_coffee', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('Cups_of_coffee')
        batch_op.drop_column('Happy_Customers')
        batch_op.drop_column('Complete_Projects')
        batch_op.drop_column('awards')

    # ### end Alembic commands ###