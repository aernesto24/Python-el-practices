class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name #only to read information
        
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = age
                
        
#to get the values
p1 = Person("Marcelo", 12)
print(p1.get_name(), " ", p1.get_age())

#We can also modify the value
p1.set_name("Gabriel")
p1.set_age(1)
print(p1.get_name(), " ", p1.get_age())


