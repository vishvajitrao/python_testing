import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from api.user import UserList, UserLists
from api.user_schema import ShowUsers
from typing import List
from fastapi import status
from fastapi import Response


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
    return Response(content=json.dumps(response), headers= {"media_type":"application/json"})


@router.get('/all-students/', tags=['Students'], response_model=List[ShowUsers])
async def all_students():
    response = {"data": None, "message": "Data fetch successfully.."}
    users = UserLists.all_users()
    response.update({"data": jsonable_encoder(users)})
    return json.dumps(response)
