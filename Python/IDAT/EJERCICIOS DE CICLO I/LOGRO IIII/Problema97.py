def cuenta_atras(numero):
    numero-=1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Fin de recursividad")

def factorial(num):
    if num>1:
        num = num * factorial(num-1)
    return num

numero = int((input("Ingrese numero: ")))

cuenta_atras(numero)
factorial(numero)