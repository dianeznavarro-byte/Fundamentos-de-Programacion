#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
dias = fecha.split("/")[0]
meses = fecha.split("/")[1]
años = fecha.split("/")[2]
print(f"El día de tu nacimiento es: {dias}")
print(f"El mes de tu nacimiento es: {meses}")   
print(f"El año de tu nacimiento es: {años}")