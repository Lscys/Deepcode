acum=int(input("Ingrese el numero de inicio de la serie: "))
cant=int(input("Ingrese el numero de terminos de la serie: "))
tot=cant
i=0
s=0

while i<tot:
    print(acum)  
    acum+=i     
    i+=1    
    s=s+acum
print(f"la suma es: {s}")
print(f"el promedio es: {s/cant}")