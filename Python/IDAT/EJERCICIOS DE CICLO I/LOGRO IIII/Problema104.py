lista=[ ]
pares=0
impares=0

i=0
x=1
for z in range(5):
    num=int(input("Ingrese numero: "))
    i+=1

    if num % x == 0:
        pares+=1
        x+1
    else:
        impares+=1
    
    lista.append(num)

print(f"Numeros ingresados {lista}")
print(f"Numeros pares {pares}")
print(f"Numeros impares {impares}")