#ejercicio 4
from pydoc import describe


articulo = int(input("Ingre precio del producto: "))
visa = int(input("Tienes tajeta VISA?[SI(1)-NO(2)]: "))


if  visa == 1:
    desc_articulo = (articulo * 20) / 100
    descuento = articulo - desc_articulo
    print("Su descuento con tajeta VISA es: ",descuento)
elif articulo > 2000:
    desc_articulo = (articulo * 20) / 100
    descuento = articulo - desc_articulo
    print("Su descuento con por el monto superior a 2000 es: ",descuento)
else:
    print("Total a pagar es: ",articulo)

