Estaturas=[ ]
mayores_promedio=0
menores_promedio=0
i=0
x=1
for z in range(5):
    altura=float(input(f"Ingrese {x} altura:"))
    i+=1
    x+=1

    if 1.70 > altura:
        menores_promedio+=1
    else:
        mayores_promedio+=1
    
    Estaturas.append(altura)

print(f"Alturas ingresadas {Estaturas}")
print(f"Mayores al promedio {mayores_promedio}")
print(f"Menores al promedio {menores_promedio}")
