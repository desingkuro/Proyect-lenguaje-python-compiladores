import random
from Operaciones import Operaciones

class Lenguaje(Operaciones):
    
    def __init__(self, elementos):
        super().__init__(elementos, tipo = Lenguaje)
        
    def generar_palabras(self, alfabetos, cantidad_palabras):
        elementos = []
        for alfabeto in alfabetos:
            elementos += ["".join(random.choices(alfabeto.elementos, k=random.randint(1, 10))) for i in range(cantidad_palabras)]
        self.elementos = elementos
        
    def get(self):
        return self.elementos
    
    def concatenacion(self, otro):
        conca = []
        for palabra1 in self.elementos:
            for palabra2 in otro.elementos:
                conca.append(palabra1 + palabra2)      
        return Lenguaje(conca)
    
    def inversa(self):
        inver = []
        for palabra in self.elementos:
            aux = list(palabra)
            aux.reverse()
            inver.append("".join(aux))
        return Lenguaje(inver)
    
    def cardinalidad(self):
        return len(self.elementos)
    
    def __str__(self):
        return f"{', '.join(self.elementos)}"

    