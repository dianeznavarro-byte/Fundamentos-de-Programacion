#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.
tiposPizza = input("¿Quieres una pizza vegetariana? (s/n): ")
if tiposPizza.lower() == "s":
    ingrediente = input("Elige un ingrediente (Pimiento/Tofu): ")
    if ingrediente.lower() == "pimiento":
        print("Has elegido una pizza vegetariana con los siguientes ingredientes: Mozzarella, Tomate y Pimiento.")
    elif ingrediente.lower() == "tofu":
        print("Has elegido una pizza vegetariana con los siguientes ingredientes: Mozzarella, Tomate y Tofu.")
else:
    ingrediente = input("Elige un ingrediente (Peperoni/Jamón/Salmón): ")
    if ingrediente.lower() == "peperoni":
        print("Has elegido una pizza no vegetariana con los siguientes ingredientes: Mozzarella, Tomate y Peperoni.")
    elif ingrediente.lower() == "jamón":
        print("Has elegido una pizza no vegetariana con los siguientes ingredientes: Mozzarella, Tomate y Jamón.")
    elif ingrediente.lower() == "salmón":
        print("Has elegido una pizza no vegetariana con los siguientes ingredientes: Mozzarella, Tomate y Salmón.")