"""About author

Revision ID: ae07457041c7
Revises: ff1ff16886a5
Create Date: 2023-01-28 01:20:30.894097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae07457041c7'
down_revision = 'ff1ff16886a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint('fk_test_user_id_user', type_='foreignkey')
        batch_op.create_foreign_key('fk_test_user_id_user', 'users', ['poster_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_author', sa.Text(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('about_author')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('fk_test_user_id_user', 'users', ['poster_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###
