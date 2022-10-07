"""
EJERCICIO 2
Desarrollar un programa que calcule el área
de las siguientes figuras: cuadrado, rectángulo,
trapecio. Dividir el programa en 4 partes, 
3 módulos, cada módulo tendrá una función que 
calcule el área de un cuadrado, de un 
rectángulo, de un trapecio y por otro lado 
un archivo que permita la ejecución de dichas 
funciones.
"""

from area_cuadrado import cuadrado
from area_rectangulo import rectangulo
from area_trapecio import trapecio

lado = int(input("Ingrese el lado del cuadrado: "))
print("El area es: ",cuadrado(lado))

base = int(input("Ingrese base del rectangulo: "))
altura = int(input("Ingrese altura del rectangulo: "))
print("El area es: ",rectangulo(base, altura))

bMayor = int(input("Ingrese la base mayor del trapecio: "))
bMenor = int(input("Ingrese la base menor del trapecio: "))
altura = int(input("Ingrese la altura del trapecio: "))
print("El area es: ",trapecio(bMayor, bMenor, altura))