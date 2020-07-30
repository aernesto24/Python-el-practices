class Person:
    
    def __init__(self, name, lastName, secondLastName):
        self.name = name
        self._last_Name = lastName  #_ indicates protected
        self.__second_last_Name = secondLastName #__ double indicates private

    def public_method(self):
        #this method only call the private method, to allow access from the outside
        self._private_method()

    def get_second_last_name(self):
        return self.__second_last_Name
    
    def set_second_last_name(self, second_last_Name):
        self.__second_last_Name = second_last_Name

    def _private_method(self): #this will define a private method
        print(self.name)
        print(self._last_Name)
        print(self.__second_last_Name)
        
p1 = Person("Ernesto", "Lopez", "Bravo")

"""if you try to access the private method directly this is what happens
p1.__private_method()  >> this line returns AttributeError: 'Person' object has no attribute '__private_method' 
To access this we will need to call the public method"""

p1.public_method()

print(p1.name)
print(p1._last_Name) #si muestra la info xq es semi protegido
# print(p1.__second_last_Name) will receive an error cuz is private
print(p1.get_second_last_name())