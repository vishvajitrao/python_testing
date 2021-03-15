from sqlalchemy import String,Integer, Column
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import aliased


Base = declarative_base()
engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    email = Column(String)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class Colleges(Base):
    __tablename__ = 'colleges'

    id = Column(Integer, primary_key=True)
    college_name = Column(String)
    location = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    users = relationship('Students', back_populates='colleges')


# Students.colleges = relationship("Colleges", order_by=Colleges.id, back_populates='users')
# Base.metadata.create_all(engine)


data = [
    {

        "name": "ABC",
        "email": "abc@gmail.com"
    },
    {

        "name": "ABC2",
        "email": "abc2@gmail.com"
    },
    {

        "name": "ABC3",
        "email": "abc3@gmail.com"
    },
    {

        "name": "ABC4",
        "email": "abc4@gmail.com"
    },
    {

        "name": "ABC5",
        "email": "abc5@gmail.com"
    },
    {

        "name": "ABC6",
        "email": "abc6@gmail.com"
    },
    {

        "name": "XYZ",
        "email": "xyz@gmail.com"
    },
    {

        "name": "XYZ",
        "email": "xyz@gmail.com"
    },
    {

        "name": "XYZ",
        "email": "xyz@gmail.com"
    },
    {

        "name": "XYZ",
        "email": "xyz@gmail.com"
    },
    {

        "name": "XYZ",
        "email": "xyz@gmail.com"
    }
]


# for student in data:
#     session.add(Students(name=student['name'], email=student['email']))
# session.commit()

# print('sucess')
# st1 = Students(name='XYZ', email='xyz@gmail.com')
# print(st1.colleges)
# st1.colleges = [Colleges(college_name='BBDU', location='Lucknow')]
# print(st1.colleges[0].users)
# session.add(st1)
# session.commit()



# #fetch data from Students
# for i in session.query(Students).all():
#     print(i)




# working with joins
# for st, col in session.query(Students, Colleges).filter(Students.id == Colleges.student_id).all():
#     print(f"{st.name} {col.college_name}")



# working with joins
# for st, col in session.query(Students, Colleges).filter(Students.id == Colleges.student_id).all():
#     print(f"{st.name} {col.college_name}")


# Use aliased
# alias1 = aliased(Colleges)
# for name, college_name in session.query(Students.name, alias1.college_name).join(Students.colleges.of_type(alias1)).filter(Students.id == alias1.student_id).all():
#     print(f"{name} {college_name}")



