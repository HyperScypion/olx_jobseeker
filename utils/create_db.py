from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database


engine = create_engine('sqlite:///../data/jobs.db')

if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData(engine)

jobs = Table('jobs', metadata,
    Column('job_id', Integer, primary_key=True),
    Column('title', String(400)),
    Column('description', Text),
    Column('location', String(100)),
    Column('link', String(500)),
    Column('salary_from', String(20)),
    Column('salary_to', String(20))
    )

jobs.create()
