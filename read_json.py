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
    text,
    Boolean,
ForeignKey

)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


# working with database with the help of SQLAlchemy
# engine = create_engine("postgresql://root:F@ntastic2021@localhost/work_packages")
engine = create_engine("postgresql://root:F@ntastic2021@127.0.0.1:5432/movtek")
print(engine)

Session = sessionmaker(bind=engine)
db = Session()
Base = declarative_base()


class CountryMaster(Base):
    __tablename__ = "country_master"

    id = Column(
        Integer,
        primary_key=True,
        index=True,

    )

    country_name = Column(String(200), unique=True)
    country_code = Column(String(10), unique=True)

    def __repr__(self):
        return "id: {}, country name: {}".format(self.id, self.country_name)


class CityMaster(Base):
    __tablename__ = "city_master"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    city_name = Column(String(200), unique=True)
    city_code = Column(String(10), unique=True)
    country_id = Column(
        Integer, ForeignKey("country_master.id", ondelete="SET NULL"), nullable=True
    )

    def __repr__(self):
        return "id: {}, city name: {}".format(self.id, self.city_name)


# data = pd.read_csv("work_packages_proj_2.csv").fillna('Null')
# print(data.columns)

# Convert all the data into the dictionary
import json
with open("data.json", "r") as json_data:
    data = json.load(json_data)

for key, value in data.items():
    code =


print("Successfully inserted...")
