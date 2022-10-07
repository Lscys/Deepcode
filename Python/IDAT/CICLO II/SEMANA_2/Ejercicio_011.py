"""
Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx". (No usar el operador *)
"""

from modulos.modulo3 import generar_n_caracteres

num = int(input("Ingrese entero: "))

caracter = "x"

print(generar_n_caracteres(num, caracter))