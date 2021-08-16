import sqlalchemy

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'mysql+mysqldb://root:Fantastic2021$@localhost/demo'
engine = sqlalchemy.create_engine(
    DATABASE_URL,
    echo_pool=True,
    pool_size=100,
    max_overflow=10,
    isolation_level="READ COMMITTED",
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DB = SessionLocal()

Base = declarative_base()




