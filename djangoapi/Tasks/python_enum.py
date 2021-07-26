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
# #
# #
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
# iteration of enum does not provide the aliases.
class Test(Enum):
    one = auto()
    two = auto()
    three = auto()
    four = auto()


print(list(Test))

# To find the aliases as well you can use __members__ attribute
print(Test.__members__)


# Allow members and attributes of the enumerations

class Laptop(Enum):
    HP = 1
    Lenovo = 2

    def describe(self):
        # self is member
        return self.name, self.value

    def __str__(self):
        return f"The value of {self.name} is {self.value}"

    @classmethod
    def custom(cls):
        return cls.Lenovo


print(Laptop.custom())
print(Laptop.HP.describe())

print("-------------------------------")
# Functional API
# A Enum class is also callable

# Enum class is also callable
fruits = Enum('Fruits', 'Apple, Banana, Orange')
for i in fruits:
    print(f"{i.name} -> {i.value}")

print("-------------------------------")
# IntEnum - The Members of IntEnum can be compared with only integrs

class Comp(IntEnum):
    com1 = 1
    com2 = 2

print(Comp == 1)
print(Comp.com2 == 2)

print("-------------------------------")
class Perm(IntFlag):
    R = 1
    W = 4
    X = 2


print(Perm.R | Perm.X)
print(Perm.R + Perm.X)
