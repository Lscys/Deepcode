"""
Definir una función que obtenga el número de elementos de una lista. (No usar len).
"""

from modulos.modulo1 import contarElementos

lista = [1, 2, 3, 4, 5, "hola", "que", "pedo", 10]

elementos = contarElementos(lista)

print("Hay {} elementos en la lista".format(elementos))