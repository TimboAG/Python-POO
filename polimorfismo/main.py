from persona import Atleta, Ciclista, Persona

def ciclista():
   ciclista = Ciclista('Ciclista')
   ciclista.moverse()   

def atleta():
   print("-"*30)
   atleta = Atleta('atleta')
   atleta.moverse()

def persona():
    print("-"*30)
    persona = Persona('Persona1')
    persona.moverse()

def main():
    ciclista()
    atleta()
    persona()


if __name__ == "__main__":
    main()