from functools import reduce
import time
from Operaciones import Operaciones

from Alfabeto import Alfabeto


Lenguajes = []

def crear_alfabetos(cantidad):
    global alfabetos
    alfabetos = []
    for i in range(cantidad):
        simbolos = input(f"Ingrese los símbolos del alfabeto {i+1} separados por comas: ").split(",")
        alfabeto = Alfabeto(simbolos)
        alfabetos.append(alfabeto)
    print(f"Se han creado {cantidad} alfabetos.")
    
def mostrarAlfabetos():
    if len(alfabetos) == 0:
        print("No se han creado alfabetos aún.")
    else:
        for i, alfabeto in enumerate(alfabetos):
            print(f"Alfabeto {i+1}: {alfabeto.get()}")
            
def opciones():
    global alfabetosSeleccionados
    aux = True
    eleccion = input(f"Ingrese los numeros de los alfabetos a los que desea realizar la unión separados por comas (1-{len(alfabetos)}): ")
    numeros = [int(opcion) for opcion in eleccion.split(",")]
    for numero in numeros:
        if numero < 1 or numero > len(alfabetos):
            print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
            aux = False
            opciones()
    if aux:
        alfabetosSeleccionados = [alfabetos[numero-1] for numero in numeros]

def menu():
    seguir=True

    while seguir:
        print("\n")
        print("|----------------------------------------------------------------------|")
        print("|                           *Bienvenido al Menu*                       |")
        print("|----------------------------------------------------------------------|")
        print("||                          *Proceso de Alfabetos*                    ||")
        print("|----------------------------------------------------------------------|")
        print("|1.Crear alfabetos                    |4.Intersección de alfabetos     |")
        print("|2.Unión de alfabetos                 |5.Calcular cerradura de estrella|")
        print("|3.Diferencia de alfabetos            |                                |")
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
    cantidad_alfabetos = int(input("Por favor, ingrese la cantidad de alfabetos a crear (minimo dos): "))
    if cantidad_alfabetos < 2:
        print("Recuerde que la cantidad mínima de alfabetos es dos. Por favor, elija otra cantidad.")
        caso_1()
    else:
        crear_alfabetos(cantidad_alfabetos)    
        
def caso_2():
    print("¿Qué alfabetos desea unir?")
    mostrarAlfabetos()
    opciones()
    union = reduce(lambda a, b: a.union(b), alfabetosSeleccionados)
    print("La union de los alfabetos seleccionados es:")
    print(union.get())
    
def caso_3():
    print("¿ De qué alfabetos deseas la diferencia?")
    mostrarAlfabetos()
    opciones = input(f"Ingrese los numeros de los alfabetos a los que desea realizar la diferncia separados por comas (1-{len(alfabetos)}): ")
    numeros = [int(opcion) for opcion in opciones.split(",")]
    alfabetosSeleccionados = [alfabetos[numero-1] for numero in numeros]
    union = reduce(lambda a, b: a.union(b), alfabetosSeleccionados)
    print("La union de los alfabetos seleccionados es:")
    print(union.get())

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
