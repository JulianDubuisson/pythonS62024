""" numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
contador = 1

while contador <= 100:
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)
    contador += 1
 """


numero1 = 0
numero2 = 1

while numero2 <= 514228:
    print(numero1, numero2, end=" ")
    numero1 = numero1 + numero2
    numero2 = numero1 + numero2
