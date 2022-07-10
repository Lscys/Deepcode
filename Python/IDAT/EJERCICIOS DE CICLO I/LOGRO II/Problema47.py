lado1 = float(input("Ingrese lado de triangulo: "))
lado2 = float(input("Ingrese lado de triangulo: "))
lado3 = float(input("Ingrese lado de triangulo: "))

perimetro_triangulo = lado1 + lado2 + lado3
print("El perimetro del triangulo es: ",perimetro_triangulo)

lado = float(input("Ingrese la base del rectangulo: "))
lado_1 = float(input("Ingrese la altura del rectangulo: "))

perimetro_rectangulo = lado + lado + lado_1 + lado_1
print("El perimetro del rectangulo es: ",perimetro_rectangulo)

if perimetro_triangulo == perimetro_rectangulo:
    print("Los perimetros coinciden")
else:
    print("Los perimetros no coinciden")