#ejercicio 9


from pydoc import describe

compra = int(input("Ingre precio de la compra del producto: "))

if  compra >= 10000:
    desc_articulo = compra *0.25
    descuento =   compra- desc_articulo
    print("Su monto a pagar es de  : ",descuento)
elif compra <10000:
    desc_articulo = compra * 0.02
    descuento =  compra-desc_articulo
    print("su monto a pagar es de : ",descuento)
else:
    print("el total  a pagar de los productos comprados es de : ",compra)