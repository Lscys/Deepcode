def convinar(cadena, caracter):
    lista = list(cadena) # separa la cadena en una lista
    nuevaCadena = caracter.join(lista)  # lo convierte en una cadena agregando un caracter en cada coma
    return nuevaCadena

def remplazar(cadena, caracter):
    return cadena.replace(" ", caracter)