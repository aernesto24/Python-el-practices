class Rectangle:
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def rectangle_area(self):
        return self.base * self.height
        
"""Enter the values for the new object"""
b = int(input("Enter the base of the rectangle: "))
h = int(input("Enter the height of the rectangle: "))

rectangle = Rectangle(b, h)
"""En el print va el nuevo objeto creado, no la clase"""
print("The Area of the rectangle is: ", rectangle.rectangle_area())

