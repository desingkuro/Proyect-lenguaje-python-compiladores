
from collections import OrderedDict


class Operaciones:
    
    def __init__(self, elementos):
        self.elementos = elementos
    
    def __str__(self):
        return f"{','.join(self.elementos)}"
    
    
    def union(self, otro):
        elementos = list(set(self.elementos) | set(otro.elementos))
        return (elementos)
    
    def diferencia(self, otro):
        elementos = list(OrderedDict.fromkeys(set(self.elementos) - set(otro.elementos)))
        return (elementos)
    
    def interseccion(self, otro):
        elementos = list(OrderedDict.fromkeys(set(self.elementos) & set(otro.elementos)))
        return (elementos)
    
    