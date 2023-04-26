import sys
from rectangulo import Rectangulo
from circulo import Circulo

def rectangulo():
    nombre= "Rectangulo"  
    aux=None
    while aux !=0:
        base=input("Ingrese base: ")
        altura= input("Ingrese altura: ")
        if base.isdigit() == False or altura.isdigit() == False:
             print("\n" * 2)
             print("-" * 25)
             print("Debe ingresar los valores correctamente")
             print("\n" * 2)
             print("-" * 25)
        else: 
            base= float(base)
            altura=float(altura)
            rectangulo = Rectangulo(base, altura,nombre)
            print("-" * 25)      
            print( rectangulo.probar_figura())
            print("-" * 25)
            break

def circulo():
    nombre= "Circulo"
    aux=1
    while aux !=0:
        radio=input("Ingrese radio: ")
        if radio.isdigit() == False:
            print("\n" * 2)
            print("-" * 25)
            print("Debe ingresar el valor del radio correctamente")
            print("-" * 25)
            print("\n" * 2)
        else: 
                radio= float(radio)            
                circulo = Circulo(nombre, radio)      
                print("-" * 25)
                print( circulo.probar_figura())
                print("-" * 25)
                break

def menu():
    opcion=0
    while opcion != 4:
        print("-" *5 , "AREA Y PERIMETRO DE FIGURAS GEOMETRICAS", "-" *5)
        opcion=input("1-Rectangurlo \n2-Circulo \n3-Salir \nIngrese una Opcion:    ")
        if opcion.isdigit() == True :
            opcion=int(opcion)
            if opcion > 0 and opcion <4:
                match opcion:
                    case 1: rectangulo()
                    case 2: circulo()
                    case _:
                        sys.exit()  
            else: 
                 print("\n" * 2)
                 print("-" * 25)
                 print("Debe elegir una opcion valida")
                 print("\n" * 2)
                 print("-" * 25)
        else:
            print("\n" * 2)
            print("-" * 25)
            print("Debe elegir una opcion valida")
            print("\n" * 2)
            print("-" * 25)

def main():
    menu()

if __name__== "__main__":
    main()

