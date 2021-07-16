from models import models
from config import DB


class UserList:
    @classmethod
    def all_users(cls):
        response = {"message": None, "data": None}
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


