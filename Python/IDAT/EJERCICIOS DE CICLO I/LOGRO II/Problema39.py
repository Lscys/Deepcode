producto = float(input("Ingrese precio producto: "))
md_pago = int(input("Forma de pago Efectivo[1], Tarjeta debito[2], Credito[3]: "))

if md_pago == 1:
    descuento = (producto * 15) / 100
    total_pago = producto - descuento
    print("Monto a pagar con Efectivo es: ",total_pago)
elif md_pago == 2 or 3:
    descuento2 = (producto * 5) / 100
    total_pago2 = producto - descuento2
    print("Monto a pagar con Tarjeta debito es: ",total_pago2)
else:
    print("Ingrese un metodo de pago [1 . 2 . 3]")
