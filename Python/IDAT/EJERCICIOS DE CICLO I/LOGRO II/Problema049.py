horas = int(input("Ingresa las horas trabajadas: " ))

if horas <= 40:
     pago = horas * 16*0.25
     
elif horas>40:
    extras = horas - 40
    pago = ((40*16) + (extras*18))*0.25

else:
    pago = (horas * 16)*0.25 

print("tu pago semanal es en total  $", pago )