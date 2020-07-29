"""Print only the numbers under 5 inside the tuple provided and store them on a list"""
numbers = (13, 1, 8, 3, 2, 5, 8)

newNumbers = []

for number in numbers:
    if number < 5:
        newNumbers.append(number)
        
print(newNumbers)