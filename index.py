import time
import os

cantidadAlfabetos = 0

class CrearListas:
    def __init__(self):
        self.lista =[]
    
    def add(self,element):
        self.lista.append(element)

    def Mostrar(self):
        print(self.lista)
    
    def cantidad(self):
        return self.lista.__len__


lista = CrearListas()

def añadirlistas(x,lista):
    alfabeto = []
    os.system('clear')
    print("|----------------------------------------------------------------------|")
    print("||                   *cuantos alfabetos desea añadir*                 ||")
    print("|----------------------------------------------------------------------|")
    cantidadAlfabetos = int(input("|-Escoja una opción:"))
    print("|----------------------------------------------------------------------|")
    for i in range(0,cantidadAlfabetos):
        print("|----------------------------------------------------------------------|")
        print(f"||       *cuantos caracteres desea añadir al alfabero {i+1}*              ||")
        print("|----------------------------------------------------------------------|")
        caracteres =int(input("|-Escoja una opción:"))
        print("|----------------------------------------------------------------------|")
        for i in range(0,caracteres):
            element = input("Ingrese el caracter: ")
            alfabeto.append(element)
        lista.add(alfabeto)

def mostrarAlfabeto(cantidadAlfabetos,lista):
    os.system('clear')
    if lista.cantidad() !=0:
        print("\n")
        print("|----------------------------------------------------------------------|")
        print("||                   *Listas de alfabetos actuales*                   ||")
        print("|----------------------------------------------------------------------|")
        lista.Mostrar()
    else:
        print("|----------------------------------------------------------------------|")
        print("||   *Nose han encontrado alfabetos, por favor ingresar alguno*       ||")
        print("|----------------------------------------------------------------------|")

def menu(lista):
    seguir=True
    os.system('clear')
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
        if opcion!=12:
            if opcion < 12 and opcion >0:
                barraDeProgreso()
                seleccion(opcion,lista)
            else:
                print("Escoja una opcion dentro del menu")
                time.sleep(1.5)
        else:
            seguir=False


def barraDeProgreso():

    total = 100
    for i in range(total):
    # Calcula el porcentaje de progreso y la cantidad de caracteres a imprimir
        porcentaje = (i / total) * 100
        caracteres = int(porcentaje / 2)
    
    # Imprime la barra de carga
        print("[{}{}] {}%".format("=" * caracteres, " " * (50 - caracteres), int(porcentaje)), end="\r")
    
    # Espera un momento antes de la siguiente iteración
        time.sleep(0.03)

    print("\n")



def seleccion(opcion,lista):
    x = int(opcion)
    switch={
        1: añadirlistas(x,lista),
        2: mostrarAlfabeto(cantidadAlfabetos,lista)
    }
        
menu(lista)



