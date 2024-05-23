"""empty message

Revision ID: 892cc55f6585
Revises: b2a2d184637f
Create Date: 2024-05-23 16:16:45.314488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '892cc55f6585'
down_revision = 'b2a2d184637f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('image1',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.LargeBinary(),
               existing_nullable=True)
        batch_op.alter_column('image2',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.LargeBinary(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('image2',
               existing_type=sa.LargeBinary(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('image1',
               existing_type=sa.LargeBinary(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###
