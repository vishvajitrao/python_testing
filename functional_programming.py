# Functional programming is programming technique where we bind the almost everything in function.
# Functional programming expected following concepts.

# 1. Pure function
#     - They generate same output for same arguments
#     - Then does not be change input argument


# Examples

#
# def pure_function(List):
#     new_list = []
#
#     for i in List:
#         new_list.append(i ** 2)
#     return new_list
#
#
# output = pure_function([1, 2, 3, 4, 5, 6])
# print(output)


# 2. Recursion

# During function programming there is no concept of while loop and for loop, instead of this recursion is used.
# Recursion is a process in which a function is call itself again and again.

# Example


# def Sum(List, index, length, s):
#     if length <= index:
#         return s
#     else:
#         s = s + List[index]
#     s = Sum(List, index + 1, length, s)
#     return s
#
#
# lst = [1, 2, 3, 4, 5, 6]
# l = len([1, 2, 3, 4, 5, 6])
# count = 0
# sum = Sum(lst, 0, l, count)
# print(sum)

# 3. Function can be higher order or First Class
# In Python programming first class function means, a function treats as a variable.They can also assign inside a variable.


# These are the major properties of first class function

# - A function is instance function of Object type
# - You can store function as variable.
# - You can pass a function as a parameter into another function.
# - You can return function from function
# - You can store them inside another variable like hash, list, etc.


# Examples


def convert_uppercase(text):
    return text.upper()


def convert_titlecase(text):
    return text.title()


def main(func):
    data = func("My name is Vishvajit Rao")
    print(data)


# if __name__ == '__main__':
#     main(convert_uppercase)
#     main(convert_titlecase)

# 4. Built-in higher order function

# Python provide various built-in higher order function which makes iterator objects list, etc much easier.


# -------------------------- Meta programming ------------------------

# In Python, metaprogramming is process to manipulate other code.
# As we know that in Python programming language, everything is associated with any type. for example integer value associated with int type, string value associated with str type.

# We have to use type() function to check the type of object.
# In Python programming, every class is also instance of type class.


class Person:
    pass


p1 = Person()

# type of p1
print(p1.__class__.__name__)

# type of Person class
print(Person.__class__.__name__)


# Create custom metaclass
# Our custom metaclass inherit from type class ans also override __init__ and __new__ method.

# __new__ method call before __init__
# __init__ method just initialize the created object passes as parameter.

# There are two ways to create metaclass in Python.

def testing(self):
    print("This is the testing method")


class Base:
    def func(self):
        print("This is the inherited method.")


# create meta class
Test = type('Test', (Base,), dict(name="Vishvait Rao", my_method=testing))

# print object name
print(Test)

# Print type of the class
print(Test.__class__.__name__)

# creating object of TestClass
t1 = Test()

# type
print(type(t1))

# calling inherited method
t1.func()

# calling instance method
t1.my_method()

# printing variable value
print(t1.name)

print('--' * 50)


# Creating meta class without using type() function directly here will inherit type class.
class TestClass(type):
    # override the __new__ method
    def __new__(cls, classname, bases, clsdict):
        print("Bases:- ", bases)
        print(type(bases))
        if len(bases) > 1:
            raise TypeError("Inherited multiple base classes!!!")
        return super().__new__(cls, classname, bases, clsdict)


# metaclass can be specified using metaclass argument.
class Base(metaclass=TestClass):
    pass


class A(Base):
    pass


class B(Base):
    pass


# class C(A, B):
#     pass


print('--' * 50)


# Python class as a decorator:- Python gives us a permission to create a class as decorator that are used to change the behaviour of existing code.
# To create decorator as a class in Python we need to just use __call__ dunder method.__call_ method. When a user need to create an object of the class tham that object act like a function.


class ClassDecorator:
    def __init__(self, function):
        print("Instance is created...")
        self.function = function
        print(self.function)

    def __call__(self):
        print("This is running...")
        self.function()


# first way to use class decorator
def printName():
    print("My name is Vishvajit")


c1 = ClassDecorator(printName)
c1()

print('--' * 10)


@ClassDecorator
def printDetails():
    print("My name is Vishvajit I am a developer!")


printDetails()

print('-- ' * 20 + 'Python Descriptors' + ' --' * 20)

# Python descriptors is the process of created to manage attributes of different classes which use the object as a reference.
# In Python descriptors we mainly use three different method __getters__(), __setters__() and __delete__().if any of these methods defined for an object that termed a descriptor. Normally Python is used getter and setter to manage attributes without any special processing.

# Implementation of descriptor in Python is pretty similar we need tom just use any of the above method.


# Creating a descriptor using class method.
class Descriptor(object):

    def __init__(self, name='Vishvajit'):
        if len(name) < 10:
            print("Assign name..")
            self.name = name
        else:
            self.name = name
            print("Your name length character shouldn't be greater than 10.")

    def __get__(self, instance, owner):
        print("Getting name....")
        return f"My name is {self.name}"

    def __set__(self, instance, name):
        print("Setting name....")
        self.name = name


    def __delete__(self, instance):
        print("Deleting name....")
        del self.name



class Student(object):
    name = Descriptor()


s1 = Student()

# getting values
print(s1.name)

# setting value
s1.name = "John"

# Getting value
print(s1.name)

# Let see what happen if we pass name whose length is greater than 10

# setting value
s1.name = "Vishvajit Rao"



# Creating a descriptor using property type

class StudentDes:
    def __init__(self, name=''):
        self.name = name

    def fget(self):
        print("Getting name....")
        return f"My name is {self.name}"

    def fset(self, value):
        print(f"Setting....{value}")
        self.name = value.title()

    def fdel(self):
        print("Deleting name....")
        del self.name

    st_name = property(fget, fset, fdel,)


sd1 = StudentDes("Coding")

# getting name
print(sd1.st_name)

# setting name
sd1.st_name = "Vishvajit"

# getting name
print(sd1.st_name)

del sd1.st_name


print('--' * 10)
# Creating descriptor using property decorator



class PersonDescriptor(object):
    def __init__(self, name):
        self.name = name


    @property
    def person_name(self):
        print("Getting name....")
        return f"My name is {self.name}"


    @person_name.setter
    def person_name(self, value):
        print(f"Setting....{value}")
        self.name = value.title()


    @person_name.deleter
    def person_name(self):
        print("Deleting name....")
        del self.name



pd1 = PersonDescriptor("Vishvajit")

# getting property name
print(pd1.person_name)

#setting property name
pd1.person_name = "Programming Funda"

# getting property name
print(pd1.person_name)






