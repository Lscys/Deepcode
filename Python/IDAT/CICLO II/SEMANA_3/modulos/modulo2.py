def dosCaracteres(cadena):
    dos = cadena[0:2]
    return dos

def tresUltimos(cadena):
    tres = cadena[-3:]
    return tres

def entreDos(cadena):
    deDos = cadena[::2]
    return deDos

def invertido(cadena):
    alReves = cadena[::-1]
    return alReves

def dobleinvertido(cadena):
    dosCaras = cadena + invertido(cadena)
    return dosCaras