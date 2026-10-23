#Escribir un programa que pida al usuario un número entero positivo y muestre porpantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Introduce un número entero positivo: "))
if numero < 1:
    print("Por favor, introduce un número entero positivo.")
else:
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i, end=", ")