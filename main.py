from functools import reduce
import time
from Alfabeto import Alfabeto
from Lenguaje import Lenguaje

alfabetos = []
lenguajes = []

def crear_alfabetos(cantidad):
    print("En este programa el elemento vacío es el #")
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
            
def opciones(objeto, mensaje):
    global seleccionados
    aux = False
    while not aux:
        eleccion = input(f"Ingrese los numeros de los {mensaje} separados por comas (1-{len(objeto)}): ")
        numeros = [int(opcion) for opcion in eleccion.split(",")]
        if len(numeros) <= 1:
            print(f"Debe elegir mínimo dos {mensaje}.")
            continue
        aux = True
        for numero in numeros:
            if numero < 1 or numero > len(objeto):
                print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(objeto)}.")
                aux = False
                break;
    if aux:
        seleccionados = [objeto[numero-1] for numero in numeros]
        
def opciones2():
    global alfabetosSeleccionados2
    aux = True
    while aux:
        eleccion = input(f"Ingrese los numeros de dos alfabetos separados por comas para utilizarlos para la creación de los dos lenguajes correspondientes (1-{len(alfabetos)}): ")
        numeros = [int(opcion) for opcion in eleccion.split(",")]
        if len(numeros) <= 1 or len(numeros) > 2:
            print("Debe elegir dos alfabetos.")
            continue
        valido = True
        for numero in numeros:
            if numero < 1 or numero > len(alfabetos):
                print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
                valido = False
                break;       
        if valido:
            alfabetosSeleccionados2 = [alfabetos[numero-1] for numero in numeros]
            break;
    
        
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
    cantidad_alfabetos = int(input("Por favor, ingrese la cantidad de alfabetos a crear (mínimo dos): "))
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
        opciones(alfabetos, "alfabetos")
        union = reduce(lambda a, b: a.union(b), seleccionados)
        print("La union de los alfabetos seleccionados es:")
        print(union.get())
    
def caso_3():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos.")
    else: 
        print("¿De qué alfabetos deseas la diferencia?")
        mostrarAlfabetos()
        opciones(alfabetos, "alfabetos")
        diferencia = reduce(lambda a, b: a.diferencia(b), seleccionados)
        print("La diferencia de los alfabetos seleccionados es:")
        print(diferencia.get())

def caso_4():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos.")
    else: 
        print("¿De qué alfabetos deseas la intersección?")
        mostrarAlfabetos()
        opciones(alfabetos, "alfabetos")
        interseccion = reduce(lambda a, b: a.interseccion(b), seleccionados)
        print("La interseccion de los alfabetos seleccionados es:")
        print(interseccion.get())

def caso_5():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos.")
    else: 
        print("¿De qué alfabeto desea la cerradura de estrellas?")
        mostrarAlfabetos()
        opcion = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alfabetos)}: "))
        while opcion < 1 or opcion > len(alfabetos):
            print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
            opcion = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alfabetos)}: ")) 
        cantidad = int(input("¿Qué cantidad de palabras quiere que haya?: "))
        print(alfabetos[opcion - 1].cerraduraEstrellas(cantidad).get())
    
def caso_6():
    if len(alfabetos) == 0:
        print("Primero debe crear los alfabetos para poder generar los lenguajes.")
    else:
        crearLenguajes()
def caso_7():
    if len(lenguajes) == 0:
        print("Primero debe crear los lenguajes.")
    else:
        print("unión de lenguajes")
        mostrarLenguajes()
        opciones(lenguajes, "lenguajes")
        union = seleccionados[0].union(seleccionados[1])
        print("La unión de los lenguajes es:")
        print(union.get())
        
def caso_8():
    if len(lenguajes) == 0:
        print("Primero debe crear los lenguajes.")
    else:
        print()
        mostrarLenguajes()
        opciones(lenguajes, "lenguajes")
        diferencia = seleccionados[0].diferencia(seleccionados[1])
        print("La diferencia de los lenguajes es:")
        print(diferencia.get())

def caso_9():
    if len(lenguajes) == 0:
        print("Primero debe crear los lenguajes.")
    else:
        print()
        mostrarLenguajes()
        opciones(lenguajes, "lenguajes")
        interseccion = seleccionados[0].interseccion(seleccionados[1])
        print("La interseccion de los lenguajes es:")
        print(interseccion.get())

def caso_10():
    if len(lenguajes) == 0:
        print("Primero debe crear los lenguajes.")
    else:
        print()
        mostrarLenguajes()
        opciones(lenguajes, "lenguajes")
        print("La concatenacion de los lenguajes es:")
        print(seleccionados[0].concatenacion(seleccionados[1]))

def caso_11():
    if len(lenguajes) == 0:
        print("Primero debe crear los lenguajes.")
    else: 
        print("¿A qué lenguaje le deseas aplicar la potencia?")
        mostrarLenguajes()
        opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
        while opcion < 1 or opcion > 2:
            print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y 2.")
            opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
        cantidad = int(input("Ingrese el valor de la potencia: "))
        print(lenguajes[opcion - 1].potencia(cantidad))

def caso_12():
    if len(lenguajes) == 0:
        print("Primero debe crear los lenguajes.")
    else: 
        print("¿A qué lenguaje le deseas aplicar la inversa?")
        mostrarLenguajes()
        opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
        while opcion < 1 or opcion > 2:
            print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y 2.")
            opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
        print(f"La inversa del lenguaje {opcion} es: ")
        print(lenguajes[opcion - 1].inversa().get())

def caso_13():
    if len(lenguajes) == 0:
        print("Primero debe crear los lenguajes.")
    else: 
        print("¿De qué lenguaje quieres obtener su cardinalidad?")
        mostrarLenguajes()
        opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
        while opcion < 1 or opcion > 2:
            print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y 2.")
            opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
        print(f"La cardinalidad del lenguaje {opcion} es: ")
        print(lenguajes[opcion - 1].cardinalidad())

if __name__ == "__main__":
    menu()
