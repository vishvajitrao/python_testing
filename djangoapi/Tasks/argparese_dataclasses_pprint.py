# steps to work with argparse module

# 1. Creating parse using ArgumentParse
# 2. Adding argument
# 3. Passing Argument


# 1st Example

# # create parser
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Process some strings")
#
# # adding argument
# parser.add_argument('integers', metavar='N', nargs='+', help='an integer for the accumulator', type=int)
#
#
# parser.add_argument(dest ='accumulate',action ='store_const',const = sum,help ='sum the integers')
#
# # parse argument
# args = parser.parse_args()
# print(args.accumulate(args.integers))


# 2nd Example

# create parser
# from argparse import ArgumentParser
# parser = ArgumentParser(description="Sort some strings")
#
# # adding argument
# parser.add_argument('integers', metavar='N', nargs='+', help='an integer for the accumulator', type=int)
#
# parser.add_argument(dest ='accumulate',action ='store_const',const = sorted,help ='arrange all the integers in '
#                                                                                   'ascending order')
#
# # parse argument
# args = parser.parse_args()
# print(args.integers)
# print(args.accumulate(args.integers))


# 3rd Example

# from argparse import ArgumentParser
# parser = ArgumentParser(description="Sort some strings")
#
# # adding argument
# parser.add_argument('integers', metavar='N', nargs='+', help='an integer for the accumulator', type=str)
#
# parser.add_argument('sum',action ='store_const',const = sum,help ='Sum of all the integers')
# parser.add_argument('len',action ='store_const',const = len,help ='len of all the integers')
#
# # parse argument
# args = parser.parse_args()
# print("All the integers:- ", args.integers)
# # print("Length the integers:- ", args.len(args.integers))
# # print("Sum the integers:- ", args.sum(args.integers))
# # print("Average is:- ", args.sum(args.integers)/args.len(args.integers))


# Dataclasses:- Python dataclasses is built-in Python module that provides decorators and functions that
# automatically generate constructor method.

from dataclasses import dataclass, field, InitVar


# Create class without dataclasses
class Students:
    def __init__(self, name, age, course):
        self.st_name = name
        self.st_age = age
        self.st_course = course

    def printDetails(self):
        print(
            f" Student name is:- {self.st_name}\n Student age is:- {self.st_age}\n Student's course is:- {self.st_course}")


s1 = Students('Vishvajit', 23, 'BCA')


# s1.printDetails()

# print("\n------- Divider --------\n")


# Using dataclasses - enable init

@dataclass(init=True)
class Student:
    name: str
    age: int
    course: str

    def printDetails(self):
        print(f" Student name is:- {self.name}\n Student age is:- {self.age}\n Student's course is:- {self.course}")

    def __str__(self):
        return "Hi! my name is Vishvajit"

    def __repr__(self):
        return f" Student name is:- {self.name}\n Student age is:- {self.age}\n Student's course is:- {self.course}"


# Using dataclasses - enable repr

# @dataclass(init=True, repr=True)
# class Student:
#     name: str
#     age: int
#     course: str
#
#     def printDetails(self):
#         print(f" Student name is:- {self.name}\n Student age is:- {self.age}\n Student's course is:- {self.course}")


# s2 = Student('Vishvajit', 23, 'BCA')
# s2.printDetails()
# print(s2)

# dataclasses - field option


@dataclass(init=True, repr=True)
class Student:
    name: str
    age: int
    marks: float = field(default=10.0, repr=False)  # default value
    courses: list = field(default_factory=list)

    def printDetails(self):
        print(
            f" Student name is:- {self.name}\n Student age is:- {self.age}\n Student's marks is:- {self.marks}\n "
            f"Student courses are:- {self.courses}")


s2 = Student('Vishvajit', 23)


# s2.printDetails()

# print("\n------- Divider --------\n")
# print(s2)
#
# print("\n------- Divider --------\n")
# s3 = Student('Vishvajit', 23, 540.20, ['Python', 'Java', 'C', 'C++', 'PHP'])
# s3.printDetails()
#
# print("\n------- Divider --------\n")


@dataclass(init=True, repr=True)
class Student:
    name: str
    age: int
    course: str
    marks: float = field(default=10.0, repr=False)  # default value

    def __post_init__(self):
        if self.course == 'PHP':
            self.marks = 0
        else:
            self.marks = 520.21

    def printDetails(self):
        print(
            f" Student name is:- {self.name}\n Student age is:- {self.age}\n Student's marks is:- {self.marks}\n "
            f"Student course is:- {self.course}")


# s4 = Student('Vishvajit', 23, 'PHP', 200)
# s4.printDetails()
# print("\n------- Divider --------\n")
#
# s4 = Student('Vishvajit', 23, 'Python', 200)
# s4.printDetails()


@dataclass(init=True, repr=True)
class Student:
    name: str
    age: int
    course: str
    accept: str = field(default=None)
    marks: float = field(default=10.0, repr=False)  # default value
    location: InitVar[str] = None

    def __post_init__(self, location):
        if location == 'noida':
            self.accept = 'Yes'
        else:
            self.accept = 'No'

    def printDetails(self):
        if self.accept == 'Yes':
            print(
                f" Student name is:- {self.name}\n Student age is:- {self.age}\n Student's marks is:- {self.marks}\n Student course is:- {self.course}")
        else:
            print("You are not eligible for this offer, please try again later")


# print("\n------- Divider --------\n")
#
# s4 = Student('Vishvajit', 23, 'Python', 'Yes', 340.20, 'noida')
# s4.printDetails()
#
# print("\n------- Divider --------\n")
#
# s4 = Student('Vishvajit', 23, 'Python', 'Yes', 340.20, 'lucknow')
# s4.printDetails()

# --------------------- Python socket module tutorial ------------------------

import socket

# get the ip of google.com
# ip = socket.gethostbyname('www.google.com')
# print(ip)

# print("\n------- Divider --------\n")
# print("Pattern 1:- ")

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()
#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()

# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()


# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(i, end='')
#     print()


# rows = 5
# spaces = rows - 1
# for i in range(1, 6):
#     for s in range(0, spaces):
#         print(end=' ')
#     spaces = spaces - 1
#
#     for v in range(1, i + 1):
#         print(v, ' ', end='')
#     print()

# rows = 5
# spaces = rows - 1
# for i in range(1, 6):
#     for s in range(0, spaces):
#         print(end=' ')
#     spaces = spaces - 1
#
#     for v in range(1, i + 1):
#         print(i, ' ', end='')
#     print()

# ---------------------------------------

# Python pprint:- Python pprint provide a capability to pretty-print arbitrary Python data structure.
from pprint import *

# data = {
#     "name": "Vishvajit Rao",
#     "age": 23,
#     "course": "BCA",
#     "profession": "Developer"
# }

# pprint(data)


# create instance of pprint
pp = PrettyPrinter(indent=4, width=30, compact=True)



# result = pformat(data, indent=6, width=20)
# print(result)

# Print the formatted representation of object followed by new line
# pp(data)


# Determine if the formatted representaion of the string is readble or not

# print(isreadable(data))
# print(isrecursive(data))
#
# # PrettyPrinter object methods
# pp.pprint(data)
# print(pp.isreadable(data))
# print(pp.isrecursive(data))
# print(pp.pformat(data))


# -------- Python cmd Module -------

# The cmd module provide simple framework for command line interface ( CLI ).To implement your own command line
# interface 





