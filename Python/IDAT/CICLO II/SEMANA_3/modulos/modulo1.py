def suma(num1, num2):
    try:
        rpta = num1 + num2
    except TypeError:
        rpta = "Tipo de dato no válido"
    return rpta

def resta(num1, num2):
    rpta = num1 - num2
    return rpta

def producto(num1, num2):
    rpta = num1 * num2
    return rpta

def division(num1, num2):
    try:
        rpta = num1 / num2
    except TypeError:
        rpta = "Tipo de dato no válido"
    except ZeroDivisionError:
        rpta = "No es posible dividir entre cero"
    return rpta
