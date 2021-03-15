import pprint




stuff =  {
"name": "Vishvajit",
"age": 22,
"course": "BCA",
"Location": "Noida"

}

#1. Prints the formatted representation of object on stream, followed by a newline.
pprint.pprint(stuff)






#2. Create the instance of PrettyPrinter class
#PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True)



stuff =  {
"name": "Vishvajit",
"age": 22,
"course": "BCA"

}

pp = pprint.PrettyPrinter(indent = 8, width = 20, depth=6)

print("Methods of PrettyPrinter")
pp.pprint(stuff)

#methods of PrettyPrinter class
print(pp.pformat(stuff))
print(pp.isreadable(stuff))
pp.pprint(stuff)

print("End the Methods of PrettyPrinter")
print("----------------------------------------")




#3. Return the formatted representation of object as a string. 
x = pprint.pformat(stuff, indent=1, width=20)
print(x)
print("----------------------------------------")






#4. Prints the formatted representation of object followed by a newline.
#pprint.pp():- If the sort_dicts is True then dictionaries key will be sorted.

data = {
"name": "Vishvajit",
"age": 22

}

pprint.pp(data, sort_dicts = True)
pprint.pp(stuff, sort_dicts = True)

print("----------------------------------------")






#5. check the format of object is readable or not.
print(pprint.isreadable(data))



