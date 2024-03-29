"""empty message

Revision ID: e81bdb2e6105
Revises: 
Create Date: 2024-02-16 09:47:20.951223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e81bdb2e6105'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chambre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('prix', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_client', sa.Integer(), nullable=True),
    sa.Column('id_chambre', sa.Integer(), nullable=True),
    sa.Column('date_arrivee', sa.DateTime(), nullable=True),
    sa.Column('date_depart', sa.DateTime(), nullable=True),
    sa.Column('statut', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['id_chambre'], ['chambre.id'], ),
    sa.ForeignKeyConstraint(['id_client'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('client')
    op.drop_table('chambre')
    # ### end Alembic commands ###
