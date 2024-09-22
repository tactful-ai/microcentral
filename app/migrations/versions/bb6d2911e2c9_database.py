"""DataBase

Revision ID: bb6d2911e2c9
Revises: 
Create Date: 2024-09-22 12:32:54.600508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb6d2911e2c9'
down_revision = None
branch_labels = None
depends_on = None

metricTypes = sa.Enum('integer', 'boolean', 'string', 'float', name='type')
criteriaTypes = sa.Enum('greater', 'smaller', 'equal', 'greater or equal', 'smaller or equal', name='criteria')

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('metric',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('type', metricTypes, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_metric_code'), 'metric', ['code'], unique=True)
    op.create_index(op.f('ix_metric_id'), 'metric', ['id'], unique=False)
    op.create_table('microservicescorecard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('microserviceId', sa.Integer(), nullable=False),
    sa.Column('scoreCardId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microservicescorecard_id'), 'microservicescorecard', ['id'], unique=False)
    op.create_table('scorecard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scorecard_id'), 'scorecard', ['id'], unique=False)
    op.create_table('scorecardmetrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scoreCardId', sa.Integer(), nullable=False),
    sa.Column('metricId', sa.Integer(), nullable=False),
    sa.Column('criteria',criteriaTypes, nullable=False),
    sa.Column('desiredValue', sa.String(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scorecardmetrics_id'), 'scorecardmetrics', ['id'], unique=False)
    op.create_table('servicemetric',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('serviceId', sa.Integer(), nullable=False),
    sa.Column('metricId', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_servicemetric_id'), 'servicemetric', ['id'], unique=False)
    op.create_table('team',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_id'), 'team', ['id'], unique=False)
    op.create_table('microservice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('teamId', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['teamId'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microservice_id'), 'microservice', ['id'], unique=False)
    metricTypes.create(op.get_bind(), checkfirst=True)
    criteriaTypes.create(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    metricTypes.drop(op.get_bind(), checkfirst=True)
    criteriaTypes.drop(op.get_bind(), checkfirst=True)
    op.drop_index(op.f('ix_microservice_id'), table_name='microservice')
    op.drop_table('microservice')
    op.drop_index(op.f('ix_team_id'), table_name='team')
    op.drop_table('team')
    op.drop_index(op.f('ix_servicemetric_id'), table_name='servicemetric')
    op.drop_table('servicemetric')
    op.drop_index(op.f('ix_scorecardmetrics_id'), table_name='scorecardmetrics')
    op.drop_table('scorecardmetrics')
    op.drop_index(op.f('ix_scorecard_id'), table_name='scorecard')
    op.drop_table('scorecard')
    op.drop_index(op.f('ix_microservicescorecard_id'), table_name='microservicescorecard')
    op.drop_table('microservicescorecard')
    op.drop_index(op.f('ix_metric_id'), table_name='metric')
    op.drop_index(op.f('ix_metric_code'), table_name='metric')
    op.drop_table('metric')
    # ### end Alembic commands ###