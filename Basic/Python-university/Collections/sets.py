"""These are examples of actions that you can execute over sets"""
#Sets has no order
#elements inside a set are unique
#elements cannot be modified, but you can add/remove element
#Sets do not have indexes

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

#delete
planets.remove(str(input("Select planet to remove: "))) #If you want to remove an element that does not exit this method provides a keyError
print(planets)

#Discard do not throw an exception if it does not find the element

planets.discard("Earth")
print(planets)

#cleat the set
planets.clear()
print(planets)

#delete the set
del planets
print(planets)

