n1=float(input("Ingrese la primera nota: "))
n2=float(input("Ingrese la segundo nota: "))
n3=float(input("Ingrese la tercer nota: "))

if n1<n2 and n1<n3:
    menor = n1
    promedio=(n2+n3)/2
if n2<n1 and n2<n3:
    menor = n2
    promedio=(n1+n3)/2
if n3<n1 and n3<n2:
    menor=n3
    promedio=(n1+n2)/2

if promedio >=10:
    print(str(promedio)+" Apronaste ")
    
else:
    print(str(promedio)+" Desapronaste ")




