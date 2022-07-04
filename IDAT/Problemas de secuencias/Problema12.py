segundos=int(input("escriba la cantidad de segundos : "))

dias=segundos//(24*60*60)
segundos=segundos%(24*60*60)
horas=segundos//(60*60)
segundos=segundos%(60*60)
minutos=segundos//60
segundos=segundos//60

print("dias:{} - horas {} - minutos {} - segundos {} ".format(dias, horas, minutos, segundos))