from Operaciones import Operaciones

class Alfabeto(Operaciones):
    
    def __init__(self, simbolos):
        super().__init__(simbolos, tipo=Alfabeto)
        
    def __str__(self):
        return f"{','.join(self.elementos)}"
    