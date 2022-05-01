# ingresante 
Horasdetrabajo = float(input("Horas a Trabajar: "))
PrecioHora = float(input("Tarifa por hora: "))

# calculo
Precio_dia = Horasdetrabajo * PrecioHora   # hora de trabajo 3.875   10.41
Precio_mes = Precio_dia * 30
#Bonificacion
Sueldo_bruto = Precio_mes+(Precio_mes * 0.20)
#Descuento
Sueldo_neto = Sueldo_bruto-(Sueldo_bruto * 0.10)

# saliente
print("Precio del Dia: ",Precio_dia)
print("Precio del Mes: ",Precio_mes)
print("Sueldo Bruto: ",Sueldo_bruto)
print("Sueldo Neto: ",Sueldo_neto)