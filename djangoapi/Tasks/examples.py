# Create a Python command line application, that take a popular name and gives some useful information related to that name from wikipedia.

from pprint import pprint
import sys
from wikipedia import *
from time import sleep

# query = ' '.join(sys.argv[1:])
# print(query)

# try:
#     wiki = wikipedia.page("laptop")
#     print("Title is:- " + wiki.title + "\n")
#     print("URL is:- ", wiki.url)
#     print("Your contents are:- ", wiki.content)

# except  exceptions.PageError:
#     print("Please enter a valid query for example:- Python, Data science")


# ---------- work with ENUM --------
from enum import *

# create a class using class

print("------------------------")


class Person(str, Enum):
    first = "Python"
    last = "Programming"


print(Person.first)
print(type(Person.first))
print(repr(Person.last))
print(Person.first.name)
print(Person.first.value)
print("------------------------")
# enumerations are iterable
for i in Person:
    print(type(i))
print("------------------------")


# ensuring unique enumeration values by using @unique decorator

# @unique
# class Number(Enum):
#     one = 1
#     two = 2
#     three = 3
#     four = 3
#
#
# print(Number)
print("------------------------")


class Numbers(Enum):
    one = auto()
    two = auto()
    three = auto()
    four = auto()


print(Numbers)

print("------------------------")


class Request(IntEnum):
    one = 1
    two = 2
    three = "3"


print(Request)

print("------------------------")
# Enum class is also callable

fruits = Enum('Fruits', 'Apple, Banana, Orange')
for i in fruits:
    print(f"{i.name} -> {i.value}")

print("-- Threading and multiprocessing ----")



