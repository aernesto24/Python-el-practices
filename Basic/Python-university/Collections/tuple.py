#similar to list but once initialized elements cannot be modified

fruits = ("apple", "pear", "orange", "peach")

print(fruits)
print(type(fruits))

#some operations that we can execute with tuples

print(len(fruits))

print(fruits[2])

#navegacion inversa
print(fruits[-1])

#working with range
print(fruits[1:3])

#to prove we cannot modify an element
#fruits[0] = "berry"
#TypeError: 'tuple' object does not support item assignment  

#to change an item in a tuple we need to converit to a list
fruitToList = list(fruits)
fruitToList[0] = "berry"


#then we can reconverted
fruits = tuple(fruitToList)
print(fruits)
print(type(fruits))

#iterate through elements
for fruit in fruits:
    print(fruit)

#to avoid printing in the next line
for fruit in fruits:
    print(fruit, end=" ")
    
del fruits
print(fruits)