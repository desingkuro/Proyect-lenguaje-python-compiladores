from Alfabeto import Alfabeto
from Lenguaje import Lenguaje


# def potencia(lenguaje, pot):
#     poten = set("#")
#     if(pot == 0):
#         return poten
#     elif(pot == 1):
#         for palabra in lenguaje:
#             poten.add(palabra)
#     else:      
#         for palabra1 in lenguaje:
#             poten.add(palabra1)
#             for palabra2 in lenguaje:
#                 poten.add(palabra1 + palabra2)
#                 poten.add(palabra2 + palabra1)
#     return poten
# def potencia(lenguaje, pot):
#     poten = set("#")
#     if(pot == 0):
#         return poten
#     elif(pot == 1):
#         for palabra in lenguaje:
#             poten.add(palabra)
#     else:      
#         for palabra1 in lenguaje:
#             for palabra2 in potencia(lenguaje, pot-1):
#                 poten.add(palabra2)
#                 poten.add(palabra1 + palabra2)
#     return poten


        
def prueba():
    a1 = Alfabeto(['a', 'g', 'c', 'f'])
    a2 = Alfabeto(['b', 'c', 'd', 'a', 'j', 'g'])
    a3 = Alfabeto(['h', 'j' , 'a'])
    # print("Alfabeto 1")
    # print(a1.get())
    # print("Alfabeto 2")
    # print(a2.get())
    # print("Alfabeto 3")
    # print(a3.get())
    # print("Union")
    # print(a1.union(a2).union(a3))
    # print("Diferencia")
    # print(a1.diferencia(a2))
    # print("Interseccion")
    # print(a1.interseccion(a2).interseccion(a3))
    # print("Cerradura de estrellas")
    # print(a1.cerraduraEstrellas(10).get())
    print("Generar lenguages")
    l1 = Lenguaje([])
    l1.generar_palabras([a1], 2)
    l2 = Lenguaje([])
    l2.generar_palabras([a2],2)
    l3 = Lenguaje([])
    l3.generar_palabras([a3],4)
    print("Languaje 1")
    print(l1.get())
    print(l1.potencia(0))
    # print("Lenguaje 2")
    # print(l2.get())
    # print("Lenguaje 3")
    # print(l3.get())
    # print("Union")
    # print(l1.union(l2).union(l3))
    # print("Diferencia")
    # print(l1.diferencia(l2))
    # print("Interseccion")
    # print(l1.interseccion(l2))
    # print("Concatenacion")
    # print(l1.concatenacion(l2))
    # # #print("Potencia")
    # # #print(potencia(l1.get(), 4))
    # print("Inverso")
    # print(l2.inversa().get())
    # print("Cardinalidad")
    # print(l2.cardinalidad())
    
if __name__ == "__main__":
    prueba()
