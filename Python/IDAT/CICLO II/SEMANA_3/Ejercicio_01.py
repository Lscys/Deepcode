"""
Crea un módulo que contenga 4 funciones para realizar la suma, resta, producto y división entre dos números.
Todas ellas devolverán el resultado. En las funciones del módulo deberá de haber tratamiento e invocación 
manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
▪ TypeError: En caso de que se envíen valores a las funciones que no sean números. Además, deberá aparecer un mensaje 
que informe Error: Tipo de dato no válido.
▪ ZeroDivisionError: En caso de realizar una división por cero. Además, deberá aparecer un mensaje que informe 
Error: No es posible dividir entre cero.
"""

from modulos.modulo1 import *

n1 = 5
n2 = 0

print(suma(n1, n2))
print(resta(n1, n2))
print(division(n1, n2))
print(producto(n1, n2))