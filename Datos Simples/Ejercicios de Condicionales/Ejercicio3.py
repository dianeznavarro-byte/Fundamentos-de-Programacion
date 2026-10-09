#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
if numero2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    numeroDivision = numero1 / numero2
    print(f"El resultado de la división es: {numeroDivision}")
    