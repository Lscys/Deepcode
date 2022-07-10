"""l1 = int(input("Ingrese longitud: "))
l2 = int(input("Ingrese longitud: "))
l3 = int(input("Ingrese longitud base: "))

if l1 and l2 and l3 == l1 and l2 and l3:
    print("Es un triangulo equilatero")
elif l1 != l2:
    print("Isoceles")
elif l1 != l2 != l3:
    print("Escaleno")
else:
    print("No forma un triangulo")"""

base=float(input("Ingrese base: "))

lado1=float(input("Ingrese lado:"))

lado2=float(input("Ingrese el segundo lado:"))

if  base<(lado1+lado2) and lado1<(lado2 + base) and lado2<(base+lado1):
 if  base==lado1 and base==lado2 :
    print("ES UN TRIANGULO EQUILATERO")
 elif  lado1==lado2 and base!=lado1 and base!=lado2 :
    print("ES UN TRIANGULO ISOCELES ")
 elif (lado1!=lado2) and (lado1!=base )and (lado2!=base):
    print("ES UN TRIANGULO ESCALENO")
else:
     print("no puede ser un triangulo ")