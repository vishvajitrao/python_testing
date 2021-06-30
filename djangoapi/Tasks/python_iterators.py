# Iterator in Python is an object that is used to iterator over iterable(list, tuple,string, etc) 

# Iterable in Python is an object that can be iterate over.List, tuple, string, etc thse all are the best examples of Python iterable.Python iterable gives an iterator when it passed into iter() method.

# iterator object gives the next value of iterable when it pass into next() method.

myList = [1,2,3,4,5]

# Traditional way to iterate above list
# for i in myList:
#     print(i)


# Iterate above list using iterator object and next() method.


# create iterator object 

iterator = iter(myList) 

# There is one more option to create iterator object that is given below
# iterator = myList.__iter__()

# get all the items of list one by one

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

#You can iterate using __next__() method
# print(iterator.__next__())


# Create a custom iterator 

class Power:
    def __init__(self, max):
        self.maximum = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.maximum:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration



# Create class object
obj = Power(5) # 0,1,2,3,4

# create iterator object
iterator = iter(obj)

# Using next to get next iteration element



print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# You can also use for loop to iteratre this 
for i in Power(8):
    print(i)










