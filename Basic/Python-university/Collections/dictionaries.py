"""These are examples of actions that you can execute over Dictionaries"""

#key value 
dictionary = {
    "AWS": "Amazon Web Services",
    "GCP": "Google Cloud Platform",
    "AZP": "Azure Cloud Platform",
    "DO": "Digital Ocean"
}

print(dictionary)
print(len(dictionary))
print(type(dictionary))

#Do not manage indexes, it uses keys

#access an element requires to specify a key
print(dictionary["GCP"])

#using Get
print( dictionary.get("AZP"))

#On dictionaries we can make changes to the key values
#dictionary[str(input("Enter the key to update: "))] = str(input("Enter the correct value: "))
dictionary["DO"] = "DigitalOcean"
print(dictionary)

#We can also iterate
for word in dictionary:
    print(word)
    
#to obtain the key's value
for word in dictionary:
    print(word + " : " + dictionary[word])
    
#return values without indicating the keys
for value in dictionary.values():
    print(value)

print(str(input("Which element are you looking for: ")) in dictionary)

#Add element
dictionary["RK"] = "RackSpace"
print(dictionary)

#Remove Element
dictionary.pop("AZP")
print(dictionary)

#Clean completely
dictionary.clear()
print(dictionary)

#delete our variable
del dictionary
print(dictionary)