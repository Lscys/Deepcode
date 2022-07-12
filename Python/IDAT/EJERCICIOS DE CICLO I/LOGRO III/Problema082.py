# Diseñe un programa que imprima y sume la siguiente serie:
# 100, 97, 94, 91, …, 16, 13, 10.

suma = 0
for x in range(100, 9, -3):
    print(x, end=" ")
    suma+=x

print("La suma es: ",suma)