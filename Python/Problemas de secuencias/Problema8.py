import math

radio=float(input("Cuanto mide el radio del cilindro: "))
altura=float(input("Cuanto mide la altura del cilindro: "))

area_base=math.pi*radio**2
area_lateral=2*math.pi*radio*altura
area_total =2*area_base*area_lateral

print("El area base del cilindro es: {:.2f}".forma(area_base))
print("El area lateral del cilindro es: {:.2f}".format(area_lateral))
print("El area total del cilindro es: {:.2f}".format(area_total))