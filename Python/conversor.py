menu = """
Bienvenido al conversor de monedas 💱

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Soles Peruanos

Eliga una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos Colombianos tiene: ")
    pesos = float(pesos)
    valor_dolar = 3926
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares ")
elif opcion == 2:
    pesos = input("Cuantos pesos Argentinos tiene: ")
    pesos = float(pesos)
    valor_dolar = 107
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares ")

elif opcion == 3:
    soles = input("Cuantos soles peruanos tiene: ")
    soles = float(soles)
    valor_dolar = 3.75
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares ")

else:
    print('Ingrese una opcion correcta porfavor')



# soles = input("Cuantos soles peruanos tiene: ")
# soles = float(soles)
# valor_dolar = 3.75
# dolares = soles / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dolares ")
