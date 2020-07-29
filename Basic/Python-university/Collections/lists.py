names = ["Juan", "Carla", "Diana", "Marcelo"]

print(names)
index = 0

for i in names:
    print(names[index])
    index += 1
    
#conocer el largo de la lista
print(len(names))

#Acceder al elemento 0
print(names[0])

#Navegacion inversa - ultimo elemento
print(names[-1])

index = -1
for i in names:
    print(names[index])
    index -= 1
    
#Recuperar un rango de nuestra lista
print(names[0:2]) #Sin incluir el indice 2 ya que recupera 2-1

#Imprimir los elementos de inicio hasta el indice proporcionado
print(names[:3]) #Sin incluir el indice 3

#Imprime los elementos de la lista que sean indice par
index = 0
for i in names:
    if index % 2 == 0 and index !=0:
        print(names[index])
    index += 1
    
#Imprimer los elementos hasta el final del indice proporcionado
print(names[2:])

#cambiar los elementos de una lista
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