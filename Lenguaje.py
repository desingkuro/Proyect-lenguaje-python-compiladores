import random
from Operaciones import Operaciones

class Lenguaje(Operaciones):
    
    def __init__(self, alfabetos, cantidad_palabras):
        elementos = []
        for alfabeto in alfabetos:
            elementos += ["".join(random.choices(alfabeto.elementos, k=random.randint(1, 10))) for i in range(cantidad_palabras)]
        super().__init__(elementos)
        
    def get(self):
        return self.elementos
    
    def __str__(self):
        return f"{', '.join(self.elementos)}"

    