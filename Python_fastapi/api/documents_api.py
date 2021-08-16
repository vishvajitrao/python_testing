from models import models
from config import DB


class DocumentsList:
    @classmethod
    def all_documents(cls):
        data = list()
        _data = DB.query(models.Document).all()
        for doc in _data:
            data.append(
                {
                    "name": doc.name,
                    "author": doc.author,
                    "authors": doc.authors
                }
            )
        return data


class DocumentsLists:
    @classmethod
    def all_documents(cls):
        response = {"message": "", "code": None, "all_documents": []}
        _data = DB.query(models.Document).all()
        # response["all_documents"]=_data
        return _data




