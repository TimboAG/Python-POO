from figura import Figura

class Rectangulo(Figura):
    
    __base=None
    __altura=None
    
    def __init__(self, base, altura, nombre):
        Figura.__init__(self, nombre)
        self.base= base 
        self.altura=altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * self.base + 2*self.altura
    
    def probar_figura(self):
        print( f"{Figura.probar_figura(self)} ") 
    
    def __str__(self) :
        return Figura.__str__(self) , " ----Base: ", self.base, " --- Altura:", self.altura