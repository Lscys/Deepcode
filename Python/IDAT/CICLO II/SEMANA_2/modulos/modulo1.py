def mayor_de_dos(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Son iguales"

def mayor_de_tres(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "Todos son iguales"

def contarElementos(lista):
    acumulador = 0
    for i in lista:
        acumulador += 1
    return acumulador
