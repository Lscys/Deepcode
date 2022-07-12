articulo = (input("Ingrese articulo: "))
precio_inicial = float(input("Ingrese precio del articulo: "))
descuento = float(input("Ingrese clave del descuento: "))

if descuento == 2:
    desc1 = (precio_inicial * 20) / 100
    precio = precio_inicial - desc1
    print("El articulo es: ",articulo)
    print("El precio con descuento es: ",precio)
elif descuento == 1:
    desc2 = (precio_inicial * 10) / 100
    precio2 = precio_inicial - desc2
    print("El articulo es: ",articulo)
    print("El precio con descuento es: ",precio2)
else:
    print(articulo)
    print(precio_inicial,"Apagar")