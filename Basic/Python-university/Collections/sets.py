#no mantienen ningun orde
#los elementos dentro del set son unicos, no pueden tener elementos duplicados
#los elementos no se pueden modificar pero si se pueden agregar/remover elementos
#tampoco tienen indice

planets = {"Mars", "Earth", "Venus", "Mercury"}

print(planets)
print(type(planets))
print(len(planets))

NotPlanets = {"Pluton", "Moon"}

#you can see if a planet is inside the set
planet = str(input("Which planet do you want to look for? "))
print(planet in planets)

planets.add(str(input("Add a planet: ")))
print(planets)

#Eliminar 
planets.remove(str(input("Select planet to remove: "))) #If you want to remove an element that does not exit this method provides a keyError
print(planets)

#Discard no arroja una execpcion si no se encuentra el element

planets.discard("Earth")
print(planets)

#limpiar set completo
planets.clear()
print(planets)

#eliminar el set
del planets
print(planets)

