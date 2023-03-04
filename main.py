import random
from Alfabeto import Alfabeto
from Lenguaje import Lenguaje


def cerraduraEstrellas(alfabeto, nPalabras):
    palabras = set()
    palabras.add("#")   
    for i in range(nPalabras):
        tamaño = random.randint(1, 2)
        palabra_aleatoria = random.sample(alfabeto, tamaño)
        palabra = "".join(palabra_aleatoria)  
        palabras.add(palabra)
    return palabras
    


def prueba():
    a1 = Alfabeto(['a', 'g', 'c', 'f'])
    a2 = Alfabeto(['b', 'c', 'd', 'a', 'j', 'g'])
    print("Alfabeto 1")
    print(a1)
    print("Alfabeto 2")
    print(a2)
    print("Union")
    print(a1.union(a2))
    print("Diferencia")
    print(a1.diferencia(a2))
    print("Interseccion")
    print(a1.interseccion(a2))
    print("Generar lenguages")
    l1 = Lenguaje([a1],2)
    l2 = Lenguaje([a2],2)
    print("Languaje 1")
    print(l1)
    print("Lenguaje 2")
    print(l2)
    print("Union")
    print(l1.union(l2))
    print("Diferencia")
    print(l1.diferencia(l2))
    print("Interseccion")
    print(l1.interseccion(l2))

    
if __name__ == "__main__":
    prueba()
