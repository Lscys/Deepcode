"""
Definir una función max_de_dos() que tome como argumento 
dos números y devuelva el mayor de ellos (No usar max).
"""
from modulos.modulo1 import mayor_de_dos

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

mayor = mayor_de_dos(num1, num2)

print("El mayor es: {}".format(mayor))
