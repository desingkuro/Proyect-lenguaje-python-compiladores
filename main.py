import random
from Alfabeto import Alfabeto
from Lenguaje import Lenguaje


def cerraduraEstrellas(alfabeto, nPalabras):
    palabras = set()
    palabras.add("#")   
    while(len(palabras) + 1 != nPalabras):
        cantR = random.randint(1, len(alfabeto))
        palabra_aleatoria = "".join(random.choices(alfabeto, k= cantR))
        palabras.add(palabra_aleatoria)
    return palabras

def concatenacion(lenguaje1, lenguaje2):
    conca = []
    for palabra1 in lenguaje1:
        for palabra2 in lenguaje2:
            conca.append(palabra1 + palabra2)      
    return conca

def potencia(lenguaje, pot):
    poten = set()
    cant = 0
    while(cant != pot):
        for palabra1 in lenguaje:
            for palabra2 in lenguaje:
                poten.add(palabra1 + palabra2)    
    return poten
        
def inversa(lenguaje):
    inver = []
    for palabra in lenguaje:
        aux = list(palabra)
        aux.reverse()
        inver.append("".join(aux))
    return inver

def cardinalidad(lenguaje):
    return len(lenguaje)
        
        
    
def prueba():
    a1 = Alfabeto(['a', 'g', 'c', 'f'])
    a2 = Alfabeto(['b', 'c', 'd', 'a', 'j', 'g'])
    print("Alfabeto 1")
    print(a1.get())
    print("Alfabeto 2")
    print(a2.get())
    print("Union")
    print(a1.union(a2))
    print("Diferencia")
    print(a1.diferencia(a2))
    print("Interseccion")
    print(a1.interseccion(a2))
    print("Cerradura de estrellas")
    print(cerraduraEstrellas(a1.get(), 50))
    print("Generar lenguages")
    l1 = Lenguaje([a1],2)
    l2 = Lenguaje([a2],15)
    print("Languaje 1")
    print(l1.get())
    print("Lenguaje 2")
    print(l2.get())
    # print("Union")
    # print(l1.union(l2))
    # print("Diferencia")
    # print(l1.diferencia(l2))
    # print("Interseccion")
    # print(l1.interseccion(l2))
    # print("Concatenacion")
    # print(concatenacion(l1.get(),l2.get()))
    # #print("Potencia")
    # #print(potencia(l1.get(), 4))
    print("Inverso")
    print(inversa(l2.get()))
    print("Cardinalidad")
    print(cardinalidad(l2.get()))
    
if __name__ == "__main__":
    prueba()
