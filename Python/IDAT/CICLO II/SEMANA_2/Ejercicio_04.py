"""
Definir una función max_de_tres(), que tome tres números 
como argumentos y devuelva el mayor de ellos (No usar max).
"""

from modulos.modulo1 import mayor_de_tres

num1 = int(input("N° 1:  "))
num2 = int(input("N° 2: "))
num3 = int(input("N° 3: "))

mayor = mayor_de_tres(num1, num2, num3)

print("El mayor es: {}".format(mayor))