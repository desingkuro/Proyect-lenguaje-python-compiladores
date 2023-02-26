import time


def menu():
    seguir=True

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
                seleccion(opcion)
            else:
                print("Escoja una opcion dentro del menu")
                time.sleep(1.5)
        else:
            seguir=False
            

def seleccion(opcion):
    x = int(opcion)
    switch={
        1:print("caso 1")
    }
        
        

menu()
