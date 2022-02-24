def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tiene: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares ")

menu = """"
Bienvenido al conversor de monedas 💱

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Soles Mexicanos

Eliga una opcion: """

opcion = int(input(menu))
if opcion == 1:
    conversor("Colombiano", 3875)
elif opcion == 2:
    conversor("Argentino", 107)
elif opcion == 3:
    conversor("Mexicano", 21)
else:
    print('Elija una opcion correcta porfavor')