from sqlalchemy import *
from uuid import uuid4
from config import Base
from sqlalchemy.orm import relationship


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
    documents = relationship("Document", back_populates="authors")


class Document(Base):
    __tablename__ = "documents"
    name = Column(String(30), primary_key=True, nullable=True)
    author = Column(String(40), ForeignKey("user.id"), nullable=True)
    authors = relationship("User", back_populates="documents")
