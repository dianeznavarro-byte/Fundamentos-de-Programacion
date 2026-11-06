#Escribir un programa que pida al usuario un número entero y muestre por pantalla sies un número primo o no.
numero = int(input("Introduce un número entero: "))
for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        print(f"{numero} no es un número primo.")
        break
else:
    print(f"{numero} es un número primo.")