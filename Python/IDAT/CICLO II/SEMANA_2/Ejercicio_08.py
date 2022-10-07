"""
Escribir una función suma() y una función producto() que sumen y multipliquen respectivamente 
todos los números de una lista. 
Por ejemplo: suma([1,2,3,4]) debería devolver 10 y producto([1,2,3,4]) debería devolver 24.
"""

from modulos.modulo2 import suma, producto

lista = [1, 2, 3, 4]

totalLista = suma(lista)
productoLista = producto(lista)

print("La suma de la lista es: ",totalLista)
print("La multiplicacion de la lista es: ",productoLista)