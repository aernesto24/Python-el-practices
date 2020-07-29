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

#no maneja indices, maneja llaves

#acceder a un elemento requiere especificar una llave
print(dictionary["GCP"])

#otra forma es con el metodo get
print( dictionary.get("AZP"))

#En los disccionarios si podemos hacer cambios en los valores asociados a una llave
#dictionary[str(input("Enter the key to update: "))] = str(input("Enter the correct value: "))
dictionary["DO"] = "DigitalOcean"
print(dictionary)

#tambien podemos iterar
for word in dictionary:
    print(word)
    
#Para regresar el valor asociado al key tambien
for word in dictionary:
    print(word + " : " + dictionary[word])
    
#una forma de devolver los valores sin indicar las llaves
for value in dictionary.values():
    print(value)

print(str(input("Which element are you looking for: ")) in dictionary)

#agregar elementos
dictionary["RK"] = "RackSpace"
print(dictionary)

#remover elementos, debemos indicar cual es el termino que queremos remover
dictionary.pop("AZP")
print(dictionary)

#limpiar completamente
dictionary.clear()
print(dictionary)

#eliminar por completo nuestra variable
del dictionary
print(dictionary)