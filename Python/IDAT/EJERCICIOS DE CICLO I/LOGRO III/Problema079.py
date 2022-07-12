# Diseñe un programa que imprima y sume la siguiente serie:
# 0,1,2,3, … ,50
i=0
suma=0
for x in range(10):
    print(i+1)
    i+=1
    suma+=i
    promedio= suma/10

print(suma)
print(f"Promedio es {promedio}")