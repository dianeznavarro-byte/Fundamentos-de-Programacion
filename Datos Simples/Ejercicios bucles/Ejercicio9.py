#Escribir un programa que almacene la cadena de caracteres contraseña en unavariable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña = "usuario"
while True:
    entrada = input("Introduce la contraseña: ")
    if entrada == contraseña:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")