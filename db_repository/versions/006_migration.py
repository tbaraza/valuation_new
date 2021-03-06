from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
data = Table('data', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('sales_amount', Integer),
    Column('cost', Integer),
    Column('expenses', Integer),
    Column('tax', Integer),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

users = Table('users', post_meta,
    Column('uid', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].columns['timestamp'].create()
    post_meta.tables['users'].columns['about_me'].create()
    post_meta.tables['users'].columns['last_seen'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].columns['timestamp'].drop()
    post_meta.tables['users'].columns['about_me'].drop()
    post_meta.tables['users'].columns['last_seen'].drop()
