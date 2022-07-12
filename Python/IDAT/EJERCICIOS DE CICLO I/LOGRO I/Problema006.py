import math 
radio=float(input("Escribre el radio del cilindro: "))
altura=float(input("Escribe la altura del cilindro: "))

volumen = math.pi * radio**2 * altura
area= (2*math.pi*radio**2) + (2*math.pi*radio*altura)
print("el area del cilindro es: {:.2f}".format(area))
print("el volumen del cilindro es: {:.2f}".format(volumen))