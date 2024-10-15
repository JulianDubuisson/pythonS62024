#Como declarar una función

""" def saludar():
    print ("Hola")
    print("¿Como estas?")
    print ("Un gusto verte")

saludar() """

""" def saludar(nombre):
    print ("Hola " + nombre)
    print("¿Como estas?")
    print ("Un gusto verte")


saludar("Julian")
saludar("Maria")
saludar("Juan") """

""" def saludar (nombre, estado):
    print ("Hola " + nombre)
    print("¿Como estas?")
    if estado == "bien":
        print("Que bueno verte bien ¿En que te puedo ayudar?")
    else:
        print ("¿En que te puedo ayudar?")

saludar(input("Escribe tu nombre: "), input("Escribe tu estado: (bien / mal)") )
saludar(input("Escribe tu nombre: "), input("Escribe tu estado: (bien / mal)") )
saludar(input("Escribe tu nombre: "), input("Escribe tu estado: (bien / mal)") )
saludar(input("Escribe tu nombre: "), input("Escribe tu estado: (bien / mal)") )
  """


def saludar (nombre, empresa, apellido):
    print("Hola " + nombre + apellido)
    print ("Bienvenido a " + empresa)
    print ("Un gusto tenerte con nosotros")




""" stock_minimo = 10
stock_actual = 25
while stock_actual > stock_minimo:
    venta = int(input("Ingrese la cantidad vendida: "))
    stock_actual -= venta
    print("Stock actual:", stock_actual)
    if stock_actual <= stock_minimo:
        print("¡Atención! El stock ha alcanzado el nivel mínimo.") 

 """
