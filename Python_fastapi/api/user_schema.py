from typing import Optional

from pydantic import BaseModel


class Users(BaseModel):
    firstName: str = None
    middleName: str = None
    lastName: str= None
    mobile_no: str= None
    landline: str= None
    emailId: str= None
    employee_id: str= None
    password: str= None


class ShowUsers(BaseModel):
    firstName: str = None
    middleName: str = None
    class Config:
        orm_mode = True

