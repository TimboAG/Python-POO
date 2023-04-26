class Figura():
    
    __nombre=None

    def __init__(self, nombre):
        self.nombre=nombre

    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def __str__(self):
            return f'{self.nombre}' 
        
    def probar_figura(self):
        return f"Figura: {self.nombre} \nArea= {self.area()} \nPerimetro= {self.perimetro()}  " 