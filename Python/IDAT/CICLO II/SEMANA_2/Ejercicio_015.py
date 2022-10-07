"""
Realizar el juego de “adivina el número”. 
Se deberá crear un programa que genere un valor aleatorio entre 1 y 100 y no se muestre. 
Después solicitar la carga de valores por teclado de un número y mostrar el mensaje “Has ganado” si el número es correcto. 
En caso contrario mostrar un mensaje informando si el número aleatorio es superior o inferior al introducido.
"""

import random

numAlatoreo = random.randint(1, 100)

print("Adivina el número", end=" ")

intentos = int(input("Ingrese numero: "))

print(numAlatoreo)

if numAlatoreo == intentos:
    print("Ganaste")
elif numAlatoreo > intentos:
    print("El numero es superior a {}".format(intentos))
else:
    print("El numero es inferior a {}".format(intentos))