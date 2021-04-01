from fastapi import FastAPI
from enum import Enum
from typing import Optional
import uuid

from pydantic import BaseModel
app = FastAPI()


# @app.get("/")
# def simple():
#     return {"name": "Vishvajit Rao"}

#Path Parameter

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

#Query parameter

# @app.get("/user")
# def simple(name: str, age: int, address: Optional[str] = "Delhi"):
#     return {"name": f"My name is {name} and i am {age} years old.I am from {address}"}


#Query parameter with type conversion
# @app.get("/user")
# async def simple(name: str, age: int, address: Optional[str] = None):
#     if address:
#         return {"name": f"My name is {name} and i am {age} years old.I am from {address}"}
#     else:
#         return {"name": f"My name is {name} and i am {age} years old."}



#Request body:- Request body are the data sent by client to the API.
# To declare a request body in the FastAPI, we will use pydantic.

class UserDetails(BaseModel):
    name: str
    username: str
    email: str
    password: str


@app.post("/user")
def simple(user_detail: UserDetails):
    return user_detail


