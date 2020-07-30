class Person:
    
    def __init__(self, name):
        self.__name = name
        self.__age = 18
        
    def get_name(self):
        return self.__name #with this method we only read information, without return this will not retunr the attrib information
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = age
                
        
#to get the values
p1 = Person("Marcelo")
print(p1.get_name(), " ", p1.get_age())

#We can also modify the value
p1.set_name("Gabriel")
p1.set_age(1)
print(p1.get_name(), " ", p1.get_age())

"""if you can edit a value outside of the class it means that it is public, python uses __ tho define a private valie
private means that it cannot be modified or read outside of the class
this is a way to protect an attribute to be modified, to modify it you need to define set and get methods
each attribute defined as private on init method needs a set/get method"""
