caracteres=[ ]
vocal=0
consonantes=0
i=0

n=int(input("Cuantos caracteres quieres ingresar?: "))

for x in range(n):
    letra=str(input("Ingrese una letra: "))
    i+=1

    if letra == "a" or letra =="e" or letra =="i" or letra =="o" or letra =="u":
        vocal+=1
    else:
        consonantes+=1

    caracteres.append(letra)

print(caracteres)
print(f"vocales {vocal}, consonantes {consonantes}")

