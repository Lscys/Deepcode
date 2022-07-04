# Genere un programa que permita el ingreso de cierta cantidad de números e indique el mayor y menor de ellos

lista = []
cantidad = int(input("cantidad: "))
mayor = 0
menor = 0
i = 1

while(cantidad > 0):
  numero = float(input("numero #" + str(i) + ": "))
  lista.append(numero)
  i = i + 1
  cantidad = cantidad - 1

mayor = max(lista)
menor = min(lista)

print("lista: ", lista)
print("mayor: ", mayor)
print("menor: ", menor)