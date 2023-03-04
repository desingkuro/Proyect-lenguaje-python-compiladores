
from collections import OrderedDict


class Operaciones:
    
    def __init__(self, elementos, tipo):
        self.elementos = elementos
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.tipo}: {','.join(self.elementos)}"
    
    
    def union(self, otro):
        elementos = list(self.elementos + otro.elementos)
        return (elementos)
    
    def diferencia(self, otro):
        elementos = list(OrderedDict.fromkeys(set(self.elementos) - set(otro.elementos)))
        return (elementos)
    
    def interseccion(self, otro):
        elementos = list(OrderedDict.fromkeys(set(self.elementos) & set(otro.elementos)))
        return (elementos)
    
    