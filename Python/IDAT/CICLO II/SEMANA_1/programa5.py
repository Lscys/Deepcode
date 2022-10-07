"""
EJECICIO 1

Realizar un programa que simule tirar
dos dados y luego muestre los
valores que aparecieron. Si la suma
de dichos números es igual a 9
mostrar un mensaje de “Has ganado”
sino mostrar “Has perdido”.
"""

from random import randint

dado1 = randint(1,6)
dado2 = randint(1,6)

print(dado1)
print(dado2)

if dado1 + dado2 == 9:
    print("Has ganado")
else:
    print("Perdiste")