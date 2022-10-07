"""
Escribir una función que tome un carácter y devuelva True 
si es una vocal, de lo contrario devuelve False
"""

from modulos.modulo2 import esVocal

caracter = input("Ingrese una letra: ")

elemento = esVocal(caracter)

print(elemento)
