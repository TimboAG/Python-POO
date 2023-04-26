class Persona:
    #la __ me dice que es privado
    __nombre=None
    __edad=None
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __metodo_privado(self):
        pass
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.nombre= nombre
        
    def  get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad  = edad
        
    def mostra_datos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)

    def __str__(self):
        return f"nombre: {self.nombre} edad: {self.edad}"