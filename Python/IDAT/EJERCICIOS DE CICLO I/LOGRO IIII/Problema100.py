def area_rectangulo(base, alt):
    ar = base * alt
    return ar
def perimetro_rectangulo(base, alt):
    per = 2*base+2*alt
    return per

for i in range(2):
    b = float(input("Ingrese la base del terreno "+str(i+1)+" : "))
    h = float(input("Ingrese la altura del terreno "+str(i+1)+" : "))
    print("El area es: ",str(area_rectangulo(b, h)))
    print("El perimetro es: ",str(perimetro_rectangulo(b, h)))
    print("-------------------------------------------------")