
lista=[ ]

i=0
j=0
for x in range(10):
    num=int(input("Ingrese numero: "))
    i+=1
    lista.append(num)

for i in lista:
    print(i, end=" ")
    j+=1

mayor=max(lista)
menor=min(lista)

print("\n"f"Numero mayor: {max(lista)}")
print(f"Numero menor: {min(lista)}")
print()
