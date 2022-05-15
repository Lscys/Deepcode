cali1 = float(input("ingresa la calificacion 1: "))
cali2 = float(input("ingresa la calificacion 2: "))
cali3 = float(input("ingresa la calificacion 3: "))
promedio = (cali1 + cali2 + cali3) / 3
if promedio >= 11:
  print("Aprobaste el curso con un promedio de: ",round(promedio,1))
else:
  print("Reprobaste el curso con un promedio de ",round(promedio,1))