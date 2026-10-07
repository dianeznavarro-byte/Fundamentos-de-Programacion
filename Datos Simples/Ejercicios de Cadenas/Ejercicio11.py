#Escribir un programa que pregunte el nombre el un producto, su precio y un númerode unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario del producto: "))
unidades = int(input("Introduce el número de unidades: "))
coste_total = precio * unidades
print(f"{nombre}: {precio:06.2f} {unidades:03d} {coste_total:08.2f}")