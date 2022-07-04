#Ingresantes
Aporte_Juan = float(input("Juan ingresa en dolares: "))
Aporte_Raquel = float(input("Raquel ingresa en dolares: "))
Aporte_Daniel = float(input("Daniel ingresa en soles: "))

#Calculo
Dolares_daniel = Aporte_Daniel/2.80
Dolares_Capital = Aporte_Juan + Aporte_Raquel + Dolares_daniel

#Porcentaje
porcentaje_juan=(Aporte_Juan*100)/Dolares_Capital
porcentaje_raquel=(Aporte_Raquel*100)/Dolares_Capital
porcentaje_daniel=(Dolares_daniel*100)/Dolares_Capital

#Salientes
print("La capital en total es: ",Dolares_Capital,"dolares")
print("Juan aporto el: ",porcentaje_juan,"%")
print("Raquel aporto el: ",porcentaje_raquel,"%")
print("Daniel aporto el: ",porcentaje_daniel,"%")
