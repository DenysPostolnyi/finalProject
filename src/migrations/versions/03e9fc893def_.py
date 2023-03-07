"""empty message

Revision ID: 03e9fc893def
Revises: 7e8e1c5ba06d
Create Date: 2023-03-02 15:46:24.271315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03e9fc893def'
down_revision = '7e8e1c5ba06d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Patients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_of_appointment', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Patients', schema=None) as batch_op:
        batch_op.drop_column('date_of_appointment')

    # ### end Alembic commands ###