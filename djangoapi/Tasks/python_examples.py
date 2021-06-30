# write a Python program to frequency of the string.
from collections import *

# 1. Without any built-in functions
string = "My name is Vishvajit Rao"
result = {}

for i in string:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

# print("Result is:- ", result)

# 2. Using dict.get

result = {}
for key in string:
    result[key] = result.get(key, 0) + 1

# print('The result is:- ', result)


# 3. Using set
result = {i: string.count(i) for i in set(string)}
print("The Result is:- ", result)

# 3. Using collection Module
# Basically Python collection module is used to improve the functionality of the collection containers.

# Counter
print(list(Counter(string).items()))


# defaultdict- defaultdict works same as Python dictionary. unlike dictionary,it does not raise KeyError when the key not exists. Using defaultdict we can specify data type of the dictionary

dictionary = defaultdict(int)
dictionary[0] = 1
# print(dictionary)

# OrderDict:- In OrderDict key maintain the order of keys.

order_dict = OrderedDict()
order_dict[0] = 1
order_dict[1] = 2
print(order_dict)

# deque - deque is going to be used to return new list.

lst = [1,2,3,4,5]
deq = deque(lst)
deq.appendleft(123)
print(deq)


# ChainMap:- It is used to combine several dictionaries or mappings

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
dict3 = { 'd' : 3, 'e' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.new_child(dict3))

# namedtuple - namedtuple returns a tuple with names for each position in the tuple.
Student = namedtuple('Student','first_name, last_name, age, email')
s1 = Student('Vishvajit', 'Rao', '22', 'vishvajitrao@gmail.com')

# Convert into dictionary
print(s1._asdict())
