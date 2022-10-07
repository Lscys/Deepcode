"""
Crear una función que reciba una cadena y un carácter y devuelva una nueva cadena con el carácter insertado 
entre cada letra de la cadena. Ej: “separar” y “,” devuelve “s,e,p,a,r,a,r”
"""

from modulos.modulo3 import convinar

cadena = input("Ingrese cadena: ")
caracter = input("Ingrese un caracter: ")

resultado = convinar(cadena, caracter)

print(resultado)