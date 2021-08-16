from models import models
from config import DB
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



class UserList:
    @classmethod
    def all_users(cls):
        data = list()
        _data = DB.query(models.User).all()
        for user in _data:
            data.append(
                {
                    "first_name": user.firstName,
                    "last_name": user.lastName,
                    "middle_name": user.middleName,
                }
            )
        return data


class UserLists:
    @classmethod
    def all_users(cls):
        _data = DB.query(models.User).all()
        return _data




