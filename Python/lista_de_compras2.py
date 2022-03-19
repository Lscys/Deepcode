lista_de_compra = []
input_de_usuario = None

print("\tPrograma lista de compra\n")

while True:
    input_de_usuario = input("¿Que desea comprar? ([Q] para salir): ")
    if input_de_usuario == "Q":
        break
    elif input_de_usuario in lista_de_compra:
        print("{} ya esta en la lista".format(input_de_usuario))
    else:
        if input("¿Seguro que quieres añadir {} a la lista de la compra? [S/N]".format(input_de_usuario)) == "S":
            lista_de_compra.append(input_de_usuario)

print("La lista de la compra es: ")
print(lista_de_compra)