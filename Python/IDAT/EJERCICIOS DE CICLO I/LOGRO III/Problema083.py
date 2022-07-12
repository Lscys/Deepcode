# Diseñe un programa que imprima y sume 10 términos de la siguiente serie:
# 9, 16, 25, 36, 49, 64, ...
i = 3
potencial=0
suma = 0
for x in range(10):
    potencial+=i**2
    print(potencial, end=" ")

    i+=1
    suma +=potencial



print("\nLa suma es: ", suma)