#Find and print only multiple of 3 bretween 1 and 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    if i % 3 == 0:
        print(i)
        
#shorter and avoiding printing 0
for i in range(10):
    if i % 3 == 0 and i != 0:
        print(i)