import random

def dividirEnteros(a, b):
    try:
        respuesta = a / b
    except TypeError:
        respuesta= "Tipo de dato no válido"
    except ZeroDivisionError:
        respuesta = "No es posible dividir entre cero"
    return respuesta

def sumarElementos(lista):
    try:
        suma = 0
        for i in lista:
            suma += i
    except TypeError:
        suma = "Un elemento de la lista no es un numero"
    return suma

def contarCaracteres(cadena):
    mayusculas = 0
    miniscular = 0
    numeros = 0
    for i in cadena:
        if i.isupper() == True:
            mayusculas +=1
        elif i.islower() == True:
            miniscular +=1
        elif i.isdigit() == True:
            numeros += 1
    return mayusculas, miniscular, numeros

def evaluarCadena(cadena):
    acum = 0
    for i in cadena:
        acum += 1
    
    if acum <= 10:
        acum = "La cadena tiene menos de 10 caracteres"
    elif acum < 20 and acum > 10:
        acum = "La cadena tiene entre 10 a 20 caracteres"
    elif acum < 50 and acum > 20:
        acum = "La cadena tiene entre 20 a 50 caracteres"
    return acum

def generarListaImpares(n):
    lista = []
    impar = []
    for i in range(n):
        lista.append(random.randint(1, 100))

    for j in lista:
        if j % 2 != 0:
            impar.append(j)
    return impar
