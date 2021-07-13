from collections import UserDict, UserList
import os
from pprint import pprint


# Custom Python Dictionary with own functionality

# 1. UserDict:- UserDict is used to when someone want to make their own dictionary with some new functionality

class MyDict(UserDict):
    # prevent from deletion

    # def __del__(self):
    #     raise RuntimeError("Deletion not allow in this dictionary")

    def pop(self, n=None):
        raise RuntimeError("Deletion not allow in this dictionary")

    def popitem(self, n=None):
        raise RuntimeError("Deletion not allow in this dictionary")

    def update(self, n=None):
        raise RuntimeError("You can't update this dictionary")


user_data = {"name": "Vishvajit", "age": 22, "email": "vishvajitrao@gmail.com"}
dct = MyDict(user_data)
dct.update({"address": "Noida"})


# --------------------------------------

# 2. Custom Python list with own functionality

