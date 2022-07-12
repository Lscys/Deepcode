#ingresantes                          
pie = float(input("Ingrese pies: "))
pulgadas = float(input("Ingrese pulgadas: "))

#Calculos
metro_pie = pie / 3.281
metro_pulgada = pulgadas / 39.37
Totalmetros = metro_pie + metro_pulgada

#salientes
print("Su estatura es: {:.2f}".format(Totalmetros),"Metros")

