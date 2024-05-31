"""empty message

Revision ID: 521918c1953d
Revises: 532bb7597315
Create Date: 2024-05-29 11:42:42.524905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '521918c1953d'
down_revision = '532bb7597315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resumes', schema=None) as batch_op:
        batch_op.alter_column('my_skill',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resumes', schema=None) as batch_op:
        batch_op.alter_column('my_skill',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###
