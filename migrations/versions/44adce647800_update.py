"""Update

Revision ID: 44adce647800
Revises: a7f0f3a59428
Create Date: 2023-01-27 15:07:06.800500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44adce647800'
down_revision = 'a7f0f3a59428'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_test_user_id_user', 'users', ['post_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('author')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint('fk_test_user_id_user', ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('post_id')

    # ### end Alembic commands ###
