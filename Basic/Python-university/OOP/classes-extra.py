    """we will show that self is not necessary,m is a convention on C is called this so we are using this
    Also we can name the parameter diff form the arguments, arguments are really created during this.name"""

class Person:

    #IF we want to pass a tupple just put * plus the var name also * indicates that the value is optional
    #to send a dictionary we use **var 
    def __init__(this, n, a, *v, **b):
        this.name = n
        this.age = a
        this.values = v
        this.books = b
    
    def deploy(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Califications (Tuple): ", self.values)
        print("Books read (Dictionary): ", self.books)
        
            
p1 = Person("Ernesto", 31)
p1.deploy()
print()
"""yo print the arguments of the class
print(p1.name)
print(p1.age)"""

#Now an example with tuple
p2 = Person("Diana", 28, 9,10,10)
p2.deploy()  
print() 

#An example with dir
p3 = Person("Marcelo", 12, 10,10,10, IT=1590, TheInstitute=697)
p3.deploy()