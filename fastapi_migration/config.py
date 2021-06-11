from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://root:F@ntastic2021@localhost/work_packages")

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
DB = Session()
Base = declarative_base()
