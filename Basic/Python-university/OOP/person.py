"""methods defined inside a class must receve self as a parameter"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#Modify values
Person.name = "Ernesto"
Person.age = 31

#Access values
print(Person.name)
print(Person.age)

#create a new object
person = Person("Marcelo", 1)
print(person.name)
print(person.age)
print(id(person))

#when creating a method self is provided by python we onlye need to write the rest of the parameters

person2 = Person("Diana", 28)
print(person2.name)
print(person2.age)
print(id(person2))