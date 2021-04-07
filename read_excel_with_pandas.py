import pandas as pd
from sqlalchemy import (
    create_engine,
    Integer,
    Text,
    Column,
    Float,
    DateTime,
    String,
    Date,
    Index,
    text,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from numpy import nan
from datetime import datetime
import json


# working with database with the help of SQLAlchemy
engine = create_engine("sqlite:///test.db")
print(engine)


Session = sessionmaker(bind=engine)
db = Session()
Base = declarative_base()


class WorkPackage(Base):
    __tablename__ = "work_packages"
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, nullable=True)
    project_id = Column(Integer, nullable=True)
    subject = Column(String, nullable=True)
    description = Column(Text)
    due_date = Column(Date)
    category_id = Column(Integer, nullable=True)
    status_id = Column(Integer, nullable=True)
    assigned_to_id = Column(Integer, nullable=True)
    priority_id = Column(Integer, server_default=text("0"), nullable=True)
    version_id = Column(Integer)
    author_id = Column(Integer, nullable=True)
    lock_version = Column(Integer, nullable=True)
    done_ratio = Column(Integer, nullable=True)
    estimated_hours = Column(Float(53), nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    start_date = Column(Date)
    responsible_id = Column(Integer, nullable=True)
    budget_id = Column(Integer, nullable=True)
    position = Column(Integer, nullable=True)
    story_points = Column(Integer, nullable=True)
    remaining_hours = Column(Float(53), nullable=True)
    derived_estimated_hours = Column(Float(53), nullable=True)
    schedule_manually = Column(Boolean, nullable=True)


# Create table
Base.metadata.create_all(engine)


# Read data from excel file
data = pd.read_excel("work_packages_v2.1.xlsx", sheet_name="work_packages_v2.1").fillna(
    "Null"
)
print(data.columns)

# Convert all the data into the dictionary
dict_data = data.to_dict(orient="record")
for i in dict_data:
    print(i)
    i.update(
        {
            "due_date": (
                datetime.strptime(str(i["due_date"]), "%Y-%m-%d %H:%M:%S")
                if str(i["due_date"]) is not "Null"
                else None
            ),
            "start_date": (
                datetime.strptime(str(i["due_date"]), "%Y-%m-%d %H:%M:%S")
                if str(i["due_date"]) is not "Null"
                else None
            ),
            "created_at": (
                datetime.strptime(str(i["due_date"]), "%Y-%m-%d %H:%M:%S")
                if str(i["due_date"]) is not "Null"
                else None
            ),
            "updated_at": (
                datetime.strptime(str(i["due_date"]), "%Y-%m-%d %H:%M:%S")
                if str(i["due_date"]) is not "Null"
                else None
            ),
        }
    )
    for key in i.keys():
        if i[key] == "Null":
            i[key] = None
    row = WorkPackage(**i)
    db.add(row)
    db.commit()


print("Successfully inserted...")
