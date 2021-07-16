from fastapi import APIRouter
from api.user import UserList
from api.user_schema import ShowUsers
from typing import List
from fastapi import status


router = APIRouter()


@router.get('/all-users/', tags=['Users'])
async def all_users():
    response = {"data": None, "message": "Data fetch successfully.."}
    users = UserList.all_users()
    response.update(
        {
            "data": users,
            "code": status.HTTP_200_OK
        }
    )
    return response



