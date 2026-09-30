#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.
novendidas = int(input("Introduce el número de barras vendidas que no son del día: "))
print("Las barras de pan del día vale: 3.49€")
descuento = 3.49 * 0.60
costefinal = descuento * novendidas
print(f"El descuento que se le hace por no ser fresca es: {descuento}€")
print(f"El coste final total es: {costefinal}€")