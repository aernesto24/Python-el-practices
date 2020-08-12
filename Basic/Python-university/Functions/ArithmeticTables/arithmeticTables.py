"""This software shows the arithmetic tables based on the input the user provides, it can show:
multiplication table, sum tablet, etc. """

#Function to provide the multiplication table from 0 to 10
def multiplicationTables(LIMIT, number):
    counter = 0
    print("Tabla de multiplicar de " + str(number))
    
    for i in range(LIMIT+1):
        result = number * counter
        print(str(number) + " * " + str(counter)+ " = " + str(result))
        counter +=1   
    
 
#Function to provide the division table from 1 to 10       
def divisionTables(LIMIT, number):
    counter = 1
    print("Tabla de dividir de " + str(number))
    
    for i in range(LIMIT+1):
        result = round(number / counter, 2)
        print(str(number) + " / " + str(counter)+ " = " + str(result))
        counter +=1 


#Function to provide the sum table from 0 to 10       
def sumTables(LIMIT, number):
    counter = 0
    print("Tabla de sumar de " + str(number))
    
    for i in range(LIMIT+1):
        result = number + counter
        print(str(number) + " + " + str(counter)+ " = " + str(result))
        counter +=1 
       

#Function to provide the substraction table from 0 to 10        
def substrationTables(LIMIT, number):
    counter = 0
    print("Tabla de restar de " + str(number))
    
    for i in range(LIMIT+1):
        result = number - counter
        print(str(number) + " - " + str(counter)+ " = " + str(result))
        counter +=1 


#Run function, here are declared the LIMIT constant and request user input for the number and option
def run():
    print("***TABLAS DE SUMA | RESTA | MULTIPLICACION | DIVISION***")
    
    LIMIT = 10
    number = int(input("Ingresa el numero para conocer su tabla: "))
    
    option = input("""Selecciona la opcion que quieres:
                   1. Tabla de multiplicacion
                   2. Tabla de division
                   3. Tabla de suma
                   4. Tabla de resta
                   5. Mostrar todas las tablas
                   : """)
    
    if option == '1':
       multiplicationTables(LIMIT, number)
    elif option == '2':
        divisionTables(LIMIT, number)
    elif option == '3':
        sumTables(LIMIT, number)
    elif option == '4':
        substrationTables(LIMIT, number)
    elif option == '5':
        multiplicationTables(LIMIT, number)
        print("")
        divisionTables(LIMIT, number)
        print("")
        multiplicationTables(LIMIT, number)
        print("")
        sumTables(LIMIT, number)
        print("")
        substrationTables(LIMIT, number)
    else:
        print("Opción invalida!!")


if __name__ == '__main__':
    run()