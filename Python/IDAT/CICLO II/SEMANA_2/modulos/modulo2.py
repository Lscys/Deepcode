import math
from posixpath import split

def esVocal(caracter):
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        return True
    elif caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        return True
    else:
        return False

def numeroVocales(cadena):
    contador = 0
    for i in cadena:
        if esVocal(i):
            contador+=1
    return contador

def suma(lista):
    total = sum(lista)
    return total

def producto(lista):
    total = math.prod(lista)
    return total

"""
def suma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def producto(lista):
    producto = 1
    for i in lista:
        producto*=i
    return producto
"""

def inversa(lista):
    listaInvertida = []
    for i in lista:
        listaInvertida.insert(0, i)
    return listaInvertida