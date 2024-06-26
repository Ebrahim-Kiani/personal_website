"""empty message

Revision ID: 11e5949352b6
Revises: ad6d12534517
Create Date: 2024-05-24 17:10:05.001102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11e5949352b6'
down_revision = 'ad6d12534517'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('informations', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('informations', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
