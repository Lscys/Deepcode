titulo = "Bienvenido a la tienda de compra de celulares"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

opcion = input("Que clase de celular deseas comprar\n"
               "A - IOS\n"
               "B - Android\n -->")


# hay_dinero = input("Tienes dinero (S/N): ")

# if hay_dinero == "S":
    # print("Felicidades, Te compraste un IOS")
# else:
    # print("No tienes dinero")

if opcion == "A" or "a":
    hay_dinero = input("Tienes dinero? [S/N]: ")
    if hay_dinero == "S" or "s":
        print("Felicidades, te comprastes un IOS")
        exit()
    else:
        print("No tienes dinero")

if opcion == "B" or "b":
    hay_dinero = input("Tienes dinero? [S/N] : ")
    if opcion == "N" or "n":
        print("No tiene dinero")
    else:
        print("Felicidades te comprastes un Androit")
        exit()


