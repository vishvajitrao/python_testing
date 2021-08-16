import json
from fastapi import APIRouter
from api.user import UserList, UserLists
from api.documents_api import DocumentsList, DocumentsLists
from fastapi import status
from fastapi import Response
from fastapi.exceptions import HTTPException
from typing import Optional
from typing import List
from api.user_schema import *
from arrow import utcnow



router = APIRouter()


@router.post('/all-users/', tags=['Users'])
async def all_users(q: Optional[str] = None):
    response = {"data": None, "message": "Data fetch successfully.."}
    users = UserList.all_users()

    response.update(
        {
            "data": users,
            "code": status.HTTP_200_OK
        }
    )
    return Response(content=json.dumps(response), media_type="application/json")


@router.get('/all-students/', tags=['Students'], description="Fetch all students", response_model=List[Users])
async def all_students():
    response = {"data": None, "message": "Data fetch successfully.."}
    a = utcnow()
    print("Today date():- ", a.date(), "Week", a.shift(days=-7).date())
    users = UserLists.all_users()
    return users


items = {"item1": "This is the first item", "item2": "This is the second item"}


@router.get("/items/{item_id}")
async def read_item(item_id: str):
    response = {"data": None, "message": None}

    if item_id not in items:
        response.update({"message": "Item not found"})
        raise HTTPException(status_code=404, detail=response)

    response.update({"data": {item_id: items[item_id]}, "message": "Data fetch successfully.."})
    return response


@router.get("/documents")
async def documents():
    response = {"data": None, "message": "Data fetch successfully.."}
    all_documents = DocumentsList.all_documents()
    response.update(
        {
            "data": all_documents
        }
    )
    return response


@router.get('/all-documents/', tags=['Documents'], description="Fetch all documents", response_model=List[AllDocuments])
async def all_documents():
    docs = DocumentsLists.all_documents()
    return docs
