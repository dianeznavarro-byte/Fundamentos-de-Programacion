#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual: "))
años = int(input("Introduce el número de años: "))
capital = cantidad * (1 + interes) ** años
print(f"El capital obtenido en la inversión es: {capital}")