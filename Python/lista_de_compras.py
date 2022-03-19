print("\tPrograma lista de la compra")

compra = input("Que desea comprar? ([Q]) para salir :")
if compra == "Q":
    exit()

primera_compra = compra 
opcion = input("Seguro que quiere añadir {} [S|N]:".format(primera_compra))
if opcion == "S":
    print("{} añadido!".format(primera_compra))
elif opcion == "N":
    print("Nose ha añadido")


compra2 = input("Que desea comprar? ([Q]) para salir :")
if compra2 == "Q":
    exit()

segunda_compra = compra2
opcion = input("Seguro que quieres añadir {} [S|N]:".format(segunda_compra))
if opcion == "S":
    print("{} añadido".format(segunda_compra))
else:
    exit()

print("La lista de la compra es:\n [{} y {}]".format(primera_compra, segunda_compra))