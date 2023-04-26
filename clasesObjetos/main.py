from clasesObjetos.persona import Persona

def crearPersona():
    persona1 = Persona("miNombre", 20)
    persona1.mostra_datos()
    # persona2 = Persona()
    # persona2.nombre = 'MiNombre'
    # persona2.edad = "20"
    # persona2.mostra_datos()

def main():
  crearPersona()  
  
if __name__ == "__main__":
    main()