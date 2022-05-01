# Ingresante
from sys import float_repr_style


Cantidad = float(input("Cantidad a comprar: "))
Precio = float(input("Precio de compra: "))

# Calculo
Subtotal = Precio*Cantidad
Primer_descuento = Subtotal-(Subtotal*0.15)
Descuento = (Subtotal*0.15)+(Primer_descuento * 0.15)
Total_pagar = Primer_descuento-(Primer_descuento * 0.15)

# Saliente
print("Importe de compra: ",Subtotal)
print("Descuento: {:.3f}".format(Descuento))
print("Total a pagar: {:.3f}".format(Total_pagar))