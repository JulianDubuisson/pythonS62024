edad = int(input("Ingrese su edad: "))
precio_completo = 20 

if edad < 0:
    print("Edad inválida. Por favor, ingrese una edad positiva.")
elif edad <= 5:
    print("¡Entrada gratuita para ti!")
elif edad <= 12:
    print("Tienes un descuento. El precio de la entrada es:", precio_completo * 0.5)
elif edad <= 65:
    print("Precio completo. El precio de la entrada es:", precio_completo)
else:
    print("¡Eres un adulto mayor! Disfruta de un descuento especial. El precio de la entrada es:", precio_completo * 0.75)
