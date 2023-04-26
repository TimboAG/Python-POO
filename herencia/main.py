from persona import Cliente, Empleado

def cliente():
   cliente1 = Cliente("Cliente1", 20)
   print(cliente1.__str__())
   cliente2 = Cliente("Cliente2", 30)
   print(cliente2.__str__())

def empleado():
   print("-"*30)
   empleado1 = Empleado("empleado1", 20, 20000)
   print(empleado1.__str__())
   empleado2 = Empleado("empleado2", 30, 100000)
   print(empleado2.__str__())

def main():
    cliente()
    empleado()

if __name__ == "__main__":
    main()