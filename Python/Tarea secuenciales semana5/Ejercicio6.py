#ejercicio 6

from pydoc import describe

articulo = int(input("Ingre precio del producto: "))


if  articulo >= 100:
    desc_articulo = articulo * 0.2
    descuento =   articulo- desc_articulo
    print("Su monto a pagar es de  : ",descuento)
elif articulo <100:
    desc_articulo = articulo * 0.05
    descuento =  articulo-desc_articulo
    print("su monto a pagar es de : ",descuento)
else:
    print("el importe a pagar es de : ",articulo)