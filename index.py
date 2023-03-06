from functools import reduce
import time
from Alfabeto import Alfabeto
from Lenguaje import Lenguaje

alfabetos = []
lenguajes = []

def crear_alfabetos(cantidad):
    for i in range(cantidad):
        simbolos = input(f"Ingrese los símbolos del alfabeto {i+1} separados por comas: ").split(",")
        alfabeto = Alfabeto(simbolos)
        alfabetos.append(alfabeto)
    print(f"Se han creado {cantidad} alfabetos.")
    
def mostrarAlfabetos():    
    for i, alfabeto in enumerate(alfabetos):
        print(f"Alfabeto {i+1}: {alfabeto.get()}")
        
def mostrarLenguajes():    
    for i, lenguaje in enumerate(lenguajes):
        print(f"Lenguaje {i+1}: {lenguaje.get()}")
            
def opciones():
    global alfabetosSeleccionados
    aux = True
    eleccion = input(f"Ingrese los numeros de los alfabetos separados por comas (1-{len(alfabetos)}): ")
    numeros = [int(opcion) for opcion in eleccion.split(",")]
    for numero in numeros:
        if numero < 1 or numero > len(alfabetos):
            print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
            aux = False
            opciones()
    if aux:
        alfabetosSeleccionados = [alfabetos[numero-1] for numero in numeros]
        
def opciones2():
    global alfabetosSeleccionados2
    aux = True
    eleccion = input(f"Ingrese los numeros de dos alfabetos separados por comas para utilizarlos para la creación de los dos lenguajes correspondientes (1-{len(alfabetos)}): ")
    numeros = [int(opcion) for opcion in eleccion.split(",")]
    for numero in numeros:
        if len(numeros) < 1 and len(numeros) > 2:
            print("Solo debe elegir dos alfabetos.")
            opciones2()
        else:
            if numero < 1 or numero > len(alfabetos):
                print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
                aux = False
                opciones2()
    if aux:
        alfabetosSeleccionados2 = [alfabetos[numero-1] for numero in numeros]
        
def crearLenguajes():
    l1 = Lenguaje([])
    l2 = Lenguaje([])
    mostrarAlfabetos()
    opciones2()
    cantidadl1 = int(input("Ingrese la cantidad de palabras que quiere que contenga el primer lenguaje: "))
    cantidadl2 = int(input("Ingrese la cantidad de palabras que quiere que contenga el segundo lenguaje: "))
    l1.generar_palabras([alfabetosSeleccionados2[0]], cantidadl1)
    l2.generar_palabras([alfabetosSeleccionados2[1]], cantidadl2)
    lenguajes.append(l1)
    lenguajes.append(l2)
    mostrarLenguajes()
    print(f"Se han creado correctamente los dos lenguajes.")

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
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos.")
    else: 
        print("¿Qué alfabetos desea unir?")
        mostrarAlfabetos()
        opciones()
        union = reduce(lambda a, b: a.union(b), alfabetosSeleccionados)
        print("La union de los alfabetos seleccionados es:")
        print(union.get())
    
def caso_3():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos.")
    else: 
        print("¿De qué alfabetos deseas la diferencia?")
        mostrarAlfabetos()
        opciones()
        diferencia = reduce(lambda a, b: a.diferencia(b), alfabetosSeleccionados)
        print("La diferencia de los alfabetos seleccionados es:")
        print(diferencia.get())

def caso_4():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos.")
    else: 
        print("¿De qué alfabetos deseas la intersección?")
        mostrarAlfabetos()
        opciones()
        interseccion = reduce(lambda a, b: a.interseccion(b), alfabetosSeleccionados)
        print("La interseccion de los alfabetos seleccionados es:")
        print(interseccion.get())

def caso_5():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos.")
    else: 
        print("¿De qué alfabeto desea la cerradura de estrellas?")
        mostrarAlfabetos()
        opcion = int(input(f"Ingrese el núnero del alfabeto {1-len(alfabetos)}: "))
        if opcion < 1 or opcion > len(alfabetos):
            print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
        else: 
            cantidad = int(input("¿Qué cantidad de palabras quiere que haya?: "))
            print(alfabetos[opcion - 1].cerraduraEstrellas(cantidad))
    
def caso_6():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos para poder generar los lenguajes.")
    else:
        crearLenguajes()
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
