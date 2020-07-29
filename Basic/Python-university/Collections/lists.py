"""These are examples of actions that you can execute over lists"""
names = ["Juan", "Carla", "Diana", "Marcelo"]

print(names)
index = 0

for i in names:
    print(names[index])
    index += 1
    
#length of the list
print(len(names))

#Access 0 element
print(names[0])

#Access last elemtn
print(names[-1])

index = -1
for i in names:
    print(names[index])
    index -= 1
    
#Return a range from the list
print(names[0:2]) #this do not include index 2 as is interpreted as 2-1

#print elements from the beginning to the index Commented
print(names[:3]) #Do not include index 3

#Print pairs from the list
index = 0
for i in names:
    if index % 2 == 0 and index !=0:
        print(names[index])
    index += 1
    
#primt elements from the index to the end
print(names[2:])

#Change elements from a list
names[1] = "Ivone"
print(names[1])

nameToSearch = str(input("Which name are you looking for? "))

if nameToSearch in names:
    print(nameToSearch + " is on the list")
else:
    print(nameToSearch + " is NOT on the list")
    
#Add a new element
names.append("Saul")
print(names)

#Insert new element en un index
names.insert(4, "Octavio")
print(names)

#remove an element
nameFour = names[4]
names.remove(nameFour)
print(names)

#remove last item
names.pop()
print(names)

#delete index provided from the list
del names[0]
print(names)

#Delete all elements from a list
names.clear()
print(names)

#erase the complete list
del names
print(names)