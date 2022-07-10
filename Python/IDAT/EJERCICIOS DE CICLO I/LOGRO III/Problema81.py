# Diseñe un programa que imprima y sume la siguiente serie:
# 10, 12, 14, …, 98, 100

suma=10
for z in range(10, 101 , 2):
    print(z, end=" ")
    suma+=z#acumlador