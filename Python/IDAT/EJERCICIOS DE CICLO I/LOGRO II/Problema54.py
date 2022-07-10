#ejercicio 5

from pydoc import describe

articulo = int(input("Ingre precio del producto: "))
visa_o_mastercard = int(input("Tienes tajeta visa_o_mastercard?[SI(1)-NO(2)]: "))

if  visa_o_mastercard == 1:
    desc_articulo = articulo * 0.15
    descuento =   articulo- desc_articulo
    print("Su descuento a pagar con tajeta VISA o MASTERCARD  es de : ",descuento)
else:
    desc_articulo = articulo *0.05
    descuento =  articulo-desc_articulo
    print("Su monto a pagar es de : ",descuento)
