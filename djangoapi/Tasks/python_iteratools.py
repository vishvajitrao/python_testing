# Python itertools module is going to used with iterator to produce complex iterators.


# 1. Infinite Operators:- Python list, tuple, set, dictionary all are the built-in iterators but it is not necessary that an iterator object has to exhaust.
import operator
from itertools import *

# 1. count():-
for i in count(5, 5):
    print(i)
    if i == 50:
        break

# 2. cycle():- This function is used to print the all the values in order from passed containers.It restart printing from beginning when all the elements are printed.

count = 0
for i in cycle('Python'):
    if count > 10:
        break
    else:
        print(i, end=' ')
        count += 1

# 3. repeat():- This function is going to be used for print a specify number infinite number of times.It will take an optional parameter num, if num is specify then it will print number of times.

print()
var = 'Python'
print(list(repeat(var, 10)))

# There are four type of combinatoric operators provided by Python itertools module.

# 1. Product():- This function is used to compute the cartesian product of the iterables.To compute the product of the iterable with itself we have to pass an optional parameter repeat.The output of this function will be tuple in sorted order.

print("The cartesian product using repeat:- ", end=' ')
print(list(product([1, 2, 3], repeat=2)))

print("The cartesian product of the containers:- ", end=' ')
print(list(product(['Python', 'Flask'], '2')))

print("The cartesian product of the containers:- ", end=' ')
print(list(product([1, 2], 'Code')))

# 2. permutations():- permutations is the process of arrange a collections of items iin different-2 ways.

print("Permutations of integer:- ")
print(list(permutations([1, 2])))

print("Permutations of string:- ")
print(list(permutations("Hi")))

# combinations():- this function is used to print all the possible combinations.

print("Combinations of integer:- ")
print(list(combinations([1, 2], 2)))

print("Combinations of string:- ")
print(list(combinations("Hi", 2)))

# In above example second argument of combinations specify the group size.


# Terminating iterators
# Terminating operators are used to work on short input sequence and produce output based on the functionality of the function.

# 1. accumulate(iterable=None, func=None):- This function takes two arguments,iterable target and functional which would be apply on each item of the iterable after iteration.If the no function passes, the addition would be apply by default.

lst = [1, 2, 3, 4, 5]
print("Print the successive summation of the elements:- ")
print(list(accumulate(iterable=lst)))

print("Print the successive multiplication of the elements:- ")
print(list(accumulate(iterable=lst, func=operator.mul)))

# 3. chain():- This function is used to print all the values of the iterable target one after another mentioned it arguments.

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]

print("Print all the elements of above three list in one single list:- ", end=' ')
print(list(chain(lst1, lst2, lst3)))

# 4. chain.from_iterable():- this function is works similarly as chain but it take list of list as an argument.

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]

lst4 = [lst1, lst2, lst3]

print("Print all the elements of above three list in one single list:- ", end=' ')
print(list(chain.from_iterable(lst4)))

# 5. compress(data=None, electors=None):- This function is going to be used for print the value from the passed container based on the passed boolean value as an argument to selector.

print("--- Python compress example ---")
var = "Python"
print(list(compress(data=var, selectors=[1, 0, 0, 1, 1, 1])))

# 6. dropwhile(): This function is going to be used to print the values from the iterable when the specify function return False for the first time.

print("dropwhile example:-")


def filterNow(i):
    if i % 2 == 0:
        return True
    else:
        return False


data = [10, 12, 3, 4, 5, 6, 7, 8, 9]
print(list(dropwhile(filterNow, data)))
print(list(dropwhile(lambda x: x % 2 == 0, data)))

# 7. filterfalse():- This function is used to print the value from the sequence when the specify function return False.

print("Python itertools filterfalse example:- ", end=' ')


def filterVowels(i):
    if i in ['i', 'e', 'o', 'u']:
        return True
    else:
        return False


name = "Python programming language"
print(list(filterfalse(filterVowels, name)))

# 8.