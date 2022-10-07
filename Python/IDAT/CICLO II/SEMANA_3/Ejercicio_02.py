"""
Crear un programa que lea una cadena y un módulo que contenga funciones para resolver lo siguiente:
• Imprimir los dos primeros caracteres de la cadena.
• Imprimir los tres últimos caracteres.
• Imprimir la cadena cada dos caracteres. Ej.: “estructura” debería imprimir “etutr”
• Imprimir la cadena en sentido inverso. Ej.: “estructura” debe imprimir “arutcrtse”
• Imprimir la cadena en un sentido y en sentido inverso. Ej: “estructura” devuelve “estructuraarutcrtse”.
"""

from modulos.modulo2 import *

cadena = "Componentes"

print(dosCaracteres(cadena))
print(tresUltimos(cadena))
print(entreDos(cadena))
print(invertido(cadena))
print(dobleinvertido(cadena))