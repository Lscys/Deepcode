acum=int(input("Ingrese el numero de inicio de la serie: "))
cantidad=int(input("Ingrese el numero de terminos de la serie: "))
total=cantidad
i=0
s=0

while i<total:
    print(acum)  
    acum+=i     
    i+=1    
    s=s+acum
print(f"la suma es: {s}")
print(f"el promedio es: {s/cantidad}")