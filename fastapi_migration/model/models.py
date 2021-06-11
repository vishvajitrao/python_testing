from sqlalchemy import String, INTEGER, Column
from fastapi_migration.config import Base


class Students(Base):
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=True)
    course = Column(String, nullable=True)
