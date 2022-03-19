numero_elegido = int(input("Ingrese un numero: "))

for n in range(1, 11):
    if n % 2 == 0:
        print("{} x {} = {}".format(n, numero_elegido, n * numero_elegido))