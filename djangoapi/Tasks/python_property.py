
# @property decorator is a python builtin decorator that can be apply any method in class and use the method as a property.


class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    # Getter
    @property
    def printEmail(self):
        email = f"{self.first_name.lower() + self.last_name.lower()}@gmail.com"
        print(email)



    # Setter
    @printEmail.setter
    def printEmail(self, first, last):
        self.first_name = first
        self.last_name = last

    # Delete
    @printEmail.deleter
    def printEmail(self):
        print("Deleting..")
        del self.first_name
        del self.last_name
        print("Completed...")





p1 = Person('Vishvajit', 'Rao')
p1.printEmail

p1.first_name = 'Kumar'
p1.last_name = 'Rao'
p1.printEmail

del p1.first_name
del p1.last_name

