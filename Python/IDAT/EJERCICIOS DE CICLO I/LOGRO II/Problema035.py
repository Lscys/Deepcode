from functools import total_ordering

trabajadores = 0

while trabajadores <= 9:
    sueldo = float(input("Ingrese sueldo mensual: "))
    venta = float(input("Monto de venta mensual: "))

    if venta > 1000:
        comision = sueldo * 0.15
        total = sueldo + comision
        print("Su ganancia del mes es: ",total)
    elif venta >= 500 and venta < 1000:
        comision = sueldo * 0.05
        total = sueldo + comision
        print("Su ganancia del mes es: ",total)
    elif venta < 500:
        print("No recibe comicion")
    trabajadores +=1
