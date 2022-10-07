"""
Desarrollar un programa que cargue una lista con “n” valores enteros. 
Cargar los valores aleatoriamente con números comprendidos entre 0 y 1000. 
Mostrar la lista obtenida por pantalla.
"""

import random

nValores = int(input("Elementos en lista: "))

lista = []

for i in range(nValores):
    lista.append(random.randint(0, 1000))

print(lista)
