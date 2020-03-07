# User defined types example

from random import random



class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def get_description(self):
        return self.name + ', ' + self.occupation



def print_person(p) -> None:
    print('Person: ' + p.get_description())
    print('Personal Lottery Number: ' + str(random()))


carl = Person('Carl von Clausewitz', 'Major-General')
print_person(carl)
