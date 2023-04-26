class Persona:
    # __nombre=None
    # __edad = None
    
    def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
        
    # def __metodo_privado(self):
    #     pass
    
    # def get_nombre(self):
    #     return self.__nombre
    
    # def set_nombre(self, nombre):
    #     self.nombre= nombre
        
    # def  get_edad(self):
    #     return self.edad
    
    # def set_edad(self, edad):
    #     self.edad  = edad
        
    def mostra_datos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)

    def __str__(self):
        return f"nombre: {self.nombre} \nedad: {self.edad}"
    
class Cliente(Persona):
        pass
    
class Empleado(Persona):
    def __init__(self, nombre, edad,   sueldo):
        #super().__init__(nombre, edad)
        Persona.__init__(self,nombre, edad)
        self.sueldo = sueldo
        
    def mostra_datos_empleado(self):
        #print( super().mostra_datos() +  f"\nSueldo: {self.sueldo}")
        print( Persona.mostra_datos(self) +  f"\nSueldo: {self.sueldo}")
        
    def __str__(self):
       # return super().__str__() + f"\nSuledo:  {self.sueldo}" 
        return Persona.__str__(self) + f"\nSuledo:  {self.sueldo}" 