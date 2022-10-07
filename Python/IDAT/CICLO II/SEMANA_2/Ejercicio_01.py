"""
-Realizar un programa que solicite la carga de un valor entero. 
-Después mostrar por pantalla la raíz cuadrada y el valor 
elevado al cuadrado y al cubo de dicho número.
(Utilizar el módulo math de python).
"""

import math

numero = int(input("Ingrese un numero entero: "))

raizCuadrada = math.sqrt(numero)  # MATH.SQRT SIRVE PARA SACAR LA RAIZ CUADRADA
cuadrado = math.pow(numero, 2)    # MATH.POW SIRVE PARA ELEVAR UN NUMERO
cubo= math.pow(numero, 3)

print("Raíz cuadrada de {} es {}".format(numero, raizCuadrada))
print("El cuadrado de {} es {}".format(numero, cuadrado))
print("El cubo de {} es {}".format(numero, cubo))