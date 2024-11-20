"""mig252

Revision ID: 0159c9ad8ec4
Revises: a537c7ffee77
Create Date: 2024-04-20 03:55:51.726481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0159c9ad8ec4'
down_revision = 'a537c7ffee77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('slug')

    # ### end Alembic commands ###
