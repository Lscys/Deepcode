"""
En el bloque principal del programa definir un diccionario que almacene los nombres de 
paises como clave y como valor la cantidad de habitantesl. Implementar un funcion
para mostrar cada clave y valor
"""

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

# Bloque principal
paises = {"Argentina":40000000, "España":460000000, "Brasil":500000000}
