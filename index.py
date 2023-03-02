import time


def menu():
    seguir = True

    while seguir:
        print("\n")
        print("|----------------------------------------------------------------------|")
        print("|                           *Bienvenido al Menu*                       |")
        print("|----------------------------------------------------------------------|")
        print("||                          *Proceso de Alfabetos*                    ||")
        print("|----------------------------------------------------------------------|")
        print("|1.Ingresar alfabeto                  |2.Unir alfabetos                |")
        print("|3.Interseccion de alfabetos          |4.Calcular cerradura de estrella|")
        print("|----------------------------------------------------------------------|")
        print("||                          *Proceso con lenguajes*                   ||")
        print("|----------------------------------------------------------------------|")
        print("|5.Generar palabras aleatorias        |6.Unión de Lenguajes            |")
        print("|7.Diferencia de lenguajes            |8.Intersección de Lenguajes     |")
        print("|9.Concatenar Lenguajes               |10.Inversa de Lenguaje          |")
        print("|11.Cardinalidad de un Lenguaje       |12.Salir                        |")
        print("|----------------------------------------------------------------------|")
        print("\n")
        opcion = int(input("Escoja una opción:"))
        if opcion != 12:
            if opcion < 12 and opcion > 0:
                seleccion(opcion)
            else:
                print("Escoja una opcion dentro del menu")
                time.sleep(1.5)
        else:
            seguir = False


def seleccion(opcion):
    x = int(opcion)
    if(x == 1):
        crear_listas()
    if(x == 2):
        mostrar_listas()

menu()


def crear_listas():

    listas = []
    nnumListas = int(input("¿Cuántas listas quieres crear? "))

    for i in range(nnumListas):
        lista = []
        numElementos = int(input(f"¿Cuántos elementos quieres en la lista {i + 1}? "))

        for j in range(numElementos):
            elemento = input(f"Ingresa el elemento {j + 1} para la lista {i + 1}: ")
            lista.append(elemento)

        listas.append(lista)

    return listas


def mostrar_listas(listas):
    for i, lista in enumerate(listas):
        print(f"Lista {i + 1}: {lista}")

    numLista = int(input("¿Qué lista deseas ver? Ingresa su número: "))
    lista_elegida = listas[numLista - 1]

    return lista_elegida

listas_creadas = crear_listas()

lista_elegida = mostrar_listas(listas_creadas)
print(f"La lista elegida es: {lista_elegida}")
