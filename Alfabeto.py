from Operaciones import Operaciones

class Alfabeto(Operaciones):
    
    def __init__(self, simbolos):
        super().__init__(simbolos)
        
    def get(self):
        return self.elementos
        
    def __str__(self):
        return f"{','.join(self.elementos)}"
    