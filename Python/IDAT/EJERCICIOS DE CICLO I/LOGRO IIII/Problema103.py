Sueldos=[ ]
x=1
i = 0
menores_200=0
mayores_150=0
for z in range(5):
    suel=int(input(f"Ingrese el {x} sueldo: " ))
    i+=1
    x+=1

    if  suel > 150:
        mayores_150+=1
    elif suel < 200:
        menores_200+=1
    
    Sueldos.append(suel)

print(f"Todos los Sueldos {Sueldos}")
print(f"Mayores a 150 son {mayores_150}")
print(f"Menores a 200 son {menores_200}")