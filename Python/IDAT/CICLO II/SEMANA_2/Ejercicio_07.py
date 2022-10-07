"""
Escribir una función que tome una cadena y devuelva el número de vocales que contiene.
"""

from modulos.modulo2 import numeroVocales

cadena = input("Ingrese cadena de texto: ")

totalVocales = numeroVocales(cadena)

print("La cadena {} tiene {} vocales en total".format(cadena, totalVocales))