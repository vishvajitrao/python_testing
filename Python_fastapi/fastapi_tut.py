from fastapi import FastAPI
from enum import Enum
from typing import Optional, List
from fastapi import Query, Path, Body, Cookie, Form, File, UploadFile
import uuid

from pydantic import BaseModel, Field

app = FastAPI()


# @app.get("/")
# def simple():
#     return {"name": "Vishvajit Rao"}

# Path Parameter

# @app.get("/user/{username}")
# def simple(username: str):
#     return {"name": username}


#
# class Gender(str, Enum):
#     male = "Male"
#     female = "Female",
#     other = "Other"
#
#
#
# @app.get("/user/{gender}")
# def simple(gender: Gender):
#     if gender == Gender.male:
#         return {"Gender": Gender.male}
#     elif gender == Gender.female:
#         return {"Gender": Gender.female}
#     else:
#         return {"Gender": Gender.other}

# Query parameter

# @app.get("/user")
# def simple(name: str, age: int, address: Optional[str] = "Delhi"):
#     return {"name": f"My name is {name} and i am {age} years old.I am from {address}"}


# Query parameter with type conversion
# @app.get("/user")
# async def simple(name: str, age: int, address: Optional[str] = None):
#     if address:
#         return {"name": f"My name is {name} and i am {age} years old.I am from {address}"}
#     else:
#         return {"name": f"My name is {name} and i am {age} years old."}


# Request body:- Request body are the data sent by client to the API.
# To declare a request body in the FastAPI, we will use Pydantic.
# pydantic:- pydantic is used to data validation and management.

# class UserDetails(BaseModel):
#     name: str
#     username: str
#     email: str
#     password: str


# @app.post("/user")
# def simple(user_detail: UserDetails):
#     return user_detail


# -----------------------------
# Query:- Query in FastApi is used to set the addition information as well as validation of the parameters.
# @app.get("/user")
# def simple(q: Optional[str] = Query(default="This is the FastApi", max_length=40)):
#     return {"name": q}

# Alias parameter
# @app.get("/user")
# def simple(q: List[str] = Query(title="Query title", description="You can pass any text in query", default=["foo", "bar"], alias="query-item")):
#     return {"name": q}

# --------------------------

# Path() in  FastAPI works same as Query().
# control the integer value limit using ge and le parameter of the Path() function

# @app.get("/user/{age}")
# def simple(age: Optional[int] = Path(default=24, title="This is title", ge=0, le=30), q: Optional[str] = Query(title="Query title", description="You can pass any text in query", default="Vishvajit Rao", alias="query-item"),
#            ):
#     return {"name": q, "age": age}


# ----------------------
# Body:- FastAPI provide Body() function to provide extra parameters for query.


class Student(BaseModel):
    roll: Optional[int]
    username: Optional[str]


class Person(BaseModel):
    name: str = Field("This is the.", title="Person Homepage")
    address: str


# without Body()

# @app.put("/user")
# def simple(student: Student, person: Person):
#     return {"name": student, "age": person}

# With the help of Body()
# @app.put("/user")
# def simple(student: Student, person: Person, description: str = Body("Noida")):
#     return {"name": student, "age": person, "description": description}

# Embed a single Body parameter
# @app.put("/user")
# def simple(
#     student: Student,
#     description: Person = Body(..., embed=True),
# ):
#     return {"name": student, "Person": description}


# Field:- Pydantic's Field is used to declare validation and metadata inside Pydantic model.
# class Person(BaseModel):
#     name: str = Field("This is the default name value", title="Person Homepage", max_length=10)
#     address: str

# Cookie:- Cookie() function is used define the cookie information like Query and Path
# Header:- Header() function is used define the header information like Query and Path


# response_model:- response_model is used to declare the model used for th response
# @app.post("/user/", response_model=Student)
# def simple(
#     student: Student
# ):
#     return {"student_details": student}

# Form Data:- To get the value from the Form you can use Form.
# @app.post("/user/")
# def simple(
#     username: str = Form('username')
# ):
#     return {"student_details": username}


# Upload file
# @app.post("/user/")
# def simple(
#     file: bytes = File("Document")
# ):
#     return {"file_size": len(file)}




