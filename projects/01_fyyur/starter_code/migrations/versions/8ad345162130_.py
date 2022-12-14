"""empty message

Revision ID: 8ad345162130
Revises: 77a717e59466
Create Date: 2022-08-11 12:36:14.858848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ad345162130'
down_revision = '77a717e59466'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('City',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['State.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('area_state')
    op.add_column('Area', sa.Column('city_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Area', 'City', ['city_id'], ['id'])
    op.drop_column('Area', 'city')
    op.alter_column('Venue', 'area_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'area_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('Area', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Area', type_='foreignkey')
    op.drop_column('Area', 'city_id')
    op.create_table('area_state',
    sa.Column('area_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('state_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['Area.id'], name='area_state_area_id_fkey'),
    sa.ForeignKeyConstraint(['state_id'], ['State.id'], name='area_state_state_id_fkey'),
    sa.PrimaryKeyConstraint('area_id', 'state_id', name='area_state_pkey')
    )
    op.drop_table('City')
    # ### end Alembic commands ###
