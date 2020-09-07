"""Determine if a number has a exact square root using 3 different algorithms"""
#Importamos time para tomar el tiempo de ejecución de cada algoritmo
import time

#definimos epsilon para 2 y 3
def define_epsilon():
    epsilon = 0
    choose_epsilon = int(input("""Selecciona el valor de epsilon a utilizar:
        1. 0.1
        2. 0.01
        3. 0.001
        : """))
    
    if choose_epsilon == 1:
        epsilon = 0.1
    elif choose_epsilon == 2:
        epsilon = 0.01
    elif  choose_epsilon == 3:
        epsilon = 0.001
    else:
        print('Opción Inválida')
    
    return epsilon


#Funcion de enumeracion exhaustiva
def enumerate(int_to_eval):
    
    while response**2 < int_to_eval:
        response +=1
        
    if response**2 == int_to_eval:
        return print(int_to_eval, 'tiene raíz cuadrada exacta, es: ', response, ' Usaste el algoritmo de enumeración exhausitva')
    else:
        return print(int_to_eval, 'NO tiene raíz cuadrada exacta',  'Usaste el algoritmo de enumeración exhausitva')


#Funcion de algoritmo de aproximacion
def aprox(int_to_eval, epsilon):
    print(epsilon)
    step = epsilon**2
    answer = 0.0
    
    while abs(answer**2 - int_to_eval) >= epsilon and answer <= int_to_eval:
        # print(abs(answer**2 - int_to_eval)) >>>> usa esto para pruebas
        answer += step
    
    if abs(answer**2 - int_to_eval) >= epsilon:
        #Si esto es true quiere decir que nos pasamos del numero
        return print('No encontramos la raiz cuadrada de: ', int_to_eval)
    else:
        return print('la raiz cuadrada de ', int_to_eval, ' es ', answer, ' con un margen de error de ', epsilon, ' Usaste el algoritmo de aproximación')


#Funcion de algoritmo busqueda binaria
def binary_search(int_to_eval, epsilon):
    low_limit = 0.0
    high_limit = max(1.0, int_to_eval)
    answer = (high_limit + low_limit) / 2

    while abs(answer**2 - int_to_eval) >= epsilon:
        # print('bajo: ', low_limit, 'alto: ', high_limit, 'respuesta:', answer) >>> usar para pruebas
        if answer ** 2 < int_to_eval:
            low_limit = answer
        else:
            high_limit = answer
        
        answer = (high_limit + low_limit) / 2
        
    return print('La raiz cuadrada de: ', int_to_eval, ' es ', answer, ' Usaste busqueda binaria')


def run():
    print("***Evaluar si un Numero tiene raíz cuadrada con 3 algoritmos***")
    question = True

    while question:
        int_to_eval = int(input("Escribe el número a evaluar: "))
    
        option = input("""Selecciona el algoritmo que quieres utilizar:
                    1. Enumeración exhaustiva
                    2. Aproximación
                    3. Búsqueda binaria
                    : """)
        
        if option == '1':
            t = time.process_time()
            enumerate(int_to_eval)
            elapsed_time = time.process_time() - t
            print('Tiempo de ejecución opcion 1 = ', elapsed_time, 'segundos')
        
        elif option == '2':
            epsilon = define_epsilon()
            t = time.process_time()
            aprox(int_to_eval, epsilon)
            elapsed_time = time.process_time() - t
            print('Tiempo de ejecución opcion 1 = ', elapsed_time, 'segundos')
        
        elif option == '3':
            epsilon = define_epsilon()
            t = time.process_time()
            binary_search(int_to_eval, epsilon)
            elapsed_time = time.process_time() - t
            print('Tiempo de ejecución opcion 1 = ', elapsed_time, 'segundos')
        
        else:
            print('Opción inválida!!')
        
        answer = input(str('\n¿Quieres probar con otro número? (si/no)'))
        
        if answer == 'si' or answer == 's':
            question = True
        elif answer == 'no' or answer == 'n':
            question = False
        else:
            print('Opción inválida!!')
            question = False
    
    
if __name__ == '__main__':
    run()