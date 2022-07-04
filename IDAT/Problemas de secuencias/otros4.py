#Un vendedor recibe un sueldo base mas un 10% extra por comisión de 
# sus ventas, el vendedor desea saber cuanto dinero obtendrá por 
# concepto de comisiones por las tres ventas que realiza en el mes y 
# el total que recibirá en el mes 
# tomando en cuenta su sueldo base y comisiones.


Sueldo = float(input("Ingrese sueldo base: "))

Primera_comision = Sueldo * 0.10
Sueldo_bruto = (Sueldo * 0.10) + 950 

Segunda_comision = Primera_comision * 0.10
Sueldo_bruto2 = (Sueldo_bruto * 0.10) 

Tercera_comision = Segunda_comision * 0.10
Sueldo_bruto3 = (Segunda_comision * 0.10) 

comision_total = Primera_comision + Segunda_comision + Tercera_comision

total_sueldo_bruto = Sueldo_bruto + Sueldo_bruto2 + Sueldo_bruto3


print(Primera_comision)
print(Segunda_comision)
print(total_sueldo_bruto)
print(comision_total)
