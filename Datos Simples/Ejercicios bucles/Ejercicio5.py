#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en porcentaje): ")) / 100
años = int(input("Introduce el número de años: "))
for año in range(1, años + 1):
    capital = cantidad * (1 + interes) ** año
    print(f"Capital al final del año {año}: {capital:.2f}")
