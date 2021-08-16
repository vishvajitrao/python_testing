from typing import Optional, List
from dataclasses import dataclass

from pydantic import BaseModel


# Documents list
class AllDocuments(BaseModel):
    name: str = None
    author: str

    class Config:
        orm_mode = True

class Users(BaseModel):
    id: str
    firstName: str = None
    middleName: str = None
    lastName: str = None
    mobile_no: str = None
    landline: str = None
    emailId: str = None
    employee_id: str = None
    password: str = None
    documents: List[AllDocuments]

    class Config():
        orm_mode = True


class ShowUsers(BaseModel):
    firstName: str = None
    middleName: str = None

    class Config():
        orm_mode = True




# class TotalDocuments(BaseModel):
#     message: str = None
#     code: int = None
#     all_documents: List[AllDocuments] = []
#
#     class Config():
#         orm_mode = True
