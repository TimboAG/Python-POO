import math
from figura import Figura

class Circulo(Figura):
    
    __radio=None
    
    def __init__(self, nombre, radio):
        Figura.__init__(self, nombre)
        self.radio =radio
        
    def area(self):
            return math.pi * self.radio * self.radio
    
    def perimetro(self):
         return 2 * math.pi * self.radio
    
    def probar_figura(self):
            print( f"{Figura.probar_figura(self)} ") 
            
    def __str__(self):
        return super().__str__(), " ---Radio: ", self.radio