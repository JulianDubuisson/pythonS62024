""" nombres = ["Tomas", "Lu", "Luli", "Virigina", "Santi", "Flor", "Orne", "Viky" ]


for nombre in nombres:
    print("Hola", nombre) """


""" stock_minimo = 10
stock_actual = 25 

while stock_actual > stock_minimo:

    venta = int(input("Ingrese la cantidad vendida: "))

    stock_actual -= venta

    print("Stock actual:", stock_actual)

    if stock_actual <= stock_minimo:
        print("¡Atención! El stock ha alcanzado el nivel mínimo.")  """



pantalones = 10
remeras = 25
buzos = 9 
bermudas = 30

while True:
    prenda= input("Ingrese el tipo de prenda a vender (pantalones, remeras, buzos, bermudas, salir): ").lower()

    if prenda == "salir":
        break


    ventas = int(input("Ingrese la cantidad de ventas: "))

    if prenda == "pantalones":
        if ventas <= pantalones:
            pantalones -= ventas
            print(f"Quedan {pantalones} en stock")
        else:
            print ("No hay suficiente stock de pantalones")

    elif prenda == "remeras":
        if ventas <= remeras:
            remeras -= ventas
            print(f"Quedan {remeras} en stock")
        else:
            print ("No hay suficiente stock de remeras")
    
    elif prenda == "buzos":
        if ventas <= buzos:
            buzos -= ventas
            print(f"Quedan {buzozs} en stock")
        else:
            print ("No hay suficiente stock de buzos")

    elif prenda == "bermudas":
        if ventas <= bermudas:
            bermudas -= ventas
            print(f"Quedan {bermudas} en stock")
        else:
            print ("No hay suficiente stock de bermudas")

    else:
        print("La prenda no es correcta")

print ("Gracias por usar JuliStock")