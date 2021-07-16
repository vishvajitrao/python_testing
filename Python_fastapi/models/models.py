from sqlalchemy import *
from uuid import uuid4
from config import Base


class User(Base):
    __tablename__ = "user"

    id = Column(
        String(40),
        default=uuid4,
        primary_key=True,
        index=True,
    )
    firstName = Column(String(50))
    middleName = Column(String(50), nullable=True)
    lastName = Column(String(50))
    mobile_no = Column(String(20))
    landline = Column(String(20), nullable=True)
    emailId = Column(String(30), unique=True)
    employee_id = Column(String(10), nullable=True)
    password = Column(String(20), nullable=True)



