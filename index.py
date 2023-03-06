import time

from Alfabeto import Alfabeto

def generar_alfabetos(cantidad_alfabetos):
    alfabetos = {}
    for i in range(cantidad_alfabetos):
        simbolos = input("Por favor, introduzca los simbolos del alfabeto separados por comas").split(",")
        nombre_alfabeto = f"alfabeto{i+1}"
        alfabetos[nombre_alfabeto] = Alfabeto(simbolos)
    return alfabetos

def menu():
    seguir=True

    while seguir:
        print("\n")
        print("|----------------------------------------------------------------------|")
        print("|                           *Bienvenido al Menu*                       |")
        print("|----------------------------------------------------------------------|")
        print("||                          *Proceso de Alfabetos*                    ||")
        print("|----------------------------------------------------------------------|")
        print("|1.Crear alfabetos                    |4.Diferencia de alfabetos       |")
        print("|2.Unión de alfabetos                 |5.Calcular cerradura de estrella|")
        print("|3.Intersección de alfabetos          |                                |")
        print("|----------------------------------------------------------------------|")
        print("||                          *Proceso con lenguajes*                   ||")
        print("|----------------------------------------------------------------------|")
        print("|6.Crear lenguajes                    |11.Potencia de un Lenguaje      |")
        print("|7.Unión de Lenguajes                 |12.Inversa de un Lenguaje       |")
        print("|8.Diferencia de lenguajes            |13.Cardinalidad de un lenguaje  |")
        print("|9.Intersección de Lenguajes          |14.Salir                        |")
        print("|10.Concatenación de lenguajes        |                                |")
        print("|----------------------------------------------------------------------|")
        print("\n")
        opcion = int(input("Escoja una opción (1-14): "))
        if opcion != 14:
            seleccion(opcion)
            time.sleep(1.5)
        else:
            seguir = False
            

def seleccion(opcion):
    x = int(opcion)
    opciones = {
        1: caso_1,
        2: caso_2,
        3: caso_3,
        4: caso_4,
        5: caso_5,
        6: caso_6,
        7: caso_7,
        8: caso_8,
        9: caso_9,
        10: caso_10,
        11: caso_11,
        12: caso_12,
        13: caso_13
    }
    opcion_elegida = opciones.get(x)
    if opcion_elegida:
        opcion_elegida()
    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 14.")
    
def caso_1():
    cantidad_alafabetos(int(input("Por favor, ingrese la cantidad de alfabetos a crear (minimo dos): ")))
    
    

def caso_2():
    pass

def caso_3():
    pass

def caso_4():
    pass

def caso_5():
    pass

def caso_6():
    pass

def caso_7():
    pass

def caso_8():
    pass

def caso_9():
    pass

def caso_10():
    pass

def caso_11():
    pass

def caso_12():
    pass

def caso_13():
    pass

menu()
