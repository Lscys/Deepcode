"""
Dado un numero que expresa el tiempo en segundos, desarrolle el programa que exprese dicho
tiempo como la cantidad de dias, horas, minutos y segundos contenidos en ese numero
"""
tiempo = int(input("Numero en segundos: "))
min = tiempo//60
hor = min//60
dias = hor // 60
print(f"La cantidad de segundos {tiempo} en minutos es {min} en horas es {hor} en dias es {dias}")