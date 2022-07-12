"""
Utilizando 2 tuplas que almacenen 2 numeros, obtener la distancia entre 
los 2 numeros(utilizar funciones)
"""

def distancia(a, b):
    t1, z1 = a
    t2, z2 = b
    return (((t2-t1)**2)+((z2-z1)**2))**0.5

x1 = int(input("Ingrese coord. x del punto 1: "))
y1 = int(input("Ingrese coord. y del punto 1: "))
x2 = int(input("Ingrese coord. x del punto 2: "))
y2 = int(input("Ingrese coord. y del punto 2: "))

p1 = (x1 , y1)
p2 = (x2 , y2)

print(f"La distancia entre los 2 puntos es: {distancia(p1, p2):.1f}")
