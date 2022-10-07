def superposicion(lista1, lista2):
    for i in lista1:
        for z in lista2:
            if i == z:
                return True
    return False

def generar_n_caracteres(num1, caracter):
    return num1 * caracter

def histograma(lista1):
    for i in lista1:
        print(i*"*")