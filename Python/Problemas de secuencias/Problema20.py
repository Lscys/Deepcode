# Ingresantes
Cantidad_dinero = int(input("Cantidad de dinero: "))

# Calculo
Primer_cambio = Cantidad_dinero // 200
Segundo_cambio = Cantidad_dinero // 100
Tercer_cambio = Cantidad_dinero // 50
Cuarto_cambio = Cantidad_dinero // 20
Quinto_cambio = Cantidad_dinero // 10
Sexto_cambio =  Cantidad_dinero // 5
Septimo_cambio = Cantidad_dinero // 2
Octavo_cambio = Cantidad_dinero // 1

# Salientes
print("En billetes de 200 hay :",Primer_cambio)
print("En billetes de 100 hay :",Segundo_cambio)
print("En billetes de 50 hay :",Tercer_cambio)
print("En billetes de 20 hay :",Cuarto_cambio)
print("En billetes de 10 hay :",Quinto_cambio)
print("En monedas de 5 hay :",Sexto_cambio)
print("En monedas de 2 hay :",Septimo_cambio)
print("En monedas de 1 hay :",Octavo_cambio)