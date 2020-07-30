#we should use self as we are inside a class
class Arirthmetic:
    
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        
    def sum(self):
        """Se realiza la operacion con los atributos de la clase
        y este es un comentario de varias lineas"""
        return self.operand1 + self.operand2
    
    def subs(self):
        return self.operand1 - self.operand2
    
    
    def mult(self):
        return self.operand1 * self.operand2
    
    def div(self):
        return self.operand1 / self.operand2
    
    

#we creaste a new object from the class and we pass the parameters inside init method

a = int(input("Insert the first number: "))
b = int(input("Insert the second number: "))

arithmetic = Arirthmetic(a, b)
print("The result of sum is: ", arithmetic.sum())
print("The result of substraction is: ", arithmetic.subs())
print("The result of multiply is: ", arithmetic.mult())
print("The result of division is: ", arithmetic.div())