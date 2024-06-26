"""empty message

Revision ID: a844839b1601
Revises: 892cc55f6585
Create Date: 2024-05-23 21:12:58.243099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a844839b1601'
down_revision = '892cc55f6585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.alter_column('image1',
               existing_type=sa.BLOB(),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.alter_column('image2',
               existing_type=sa.BLOB(),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.drop_column('DateOfBirth')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('DateOfBirth', sa.DATETIME(), nullable=True))
        batch_op.alter_column('image2',
               existing_type=sa.String(length=255),
               type_=sa.BLOB(),
               existing_nullable=True)
        batch_op.alter_column('image1',
               existing_type=sa.String(length=255),
               type_=sa.BLOB(),
               existing_nullable=True)
        batch_op.drop_column('age')

    # ### end Alembic commands ###
