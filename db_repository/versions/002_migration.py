from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('firstname', VARCHAR(length=64)),
    Column('lastname', VARCHAR(length=64)),
    Column('nickname', VARCHAR(length=64), nullable=False),
    Column('password_hash', VARCHAR(length=64), nullable=False),
    Column('email', VARCHAR(length=120)),
    Column('role', SMALLINT),
    Column('is_active', SMALLINT),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['is_active'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['is_active'].create()
