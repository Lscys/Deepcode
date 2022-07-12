kilometro = float(input("Kilometros a recorrer?: "))
pies = float(input("Pies ha recorrer?: "))
millas = float(input("Millas ha recorrer?: "))
#calculos
PrimerTramo =kilometro*1000
Segundotramo=pies/3.2808
Tercertramo=millas*1609
metro = 3.2808  # pies  """Un metro"""
milla = 1609    # metros """Una milla"""

totalmetros = PrimerTramo + Segundotramo + Tercertramo
totalyardas = totalmetros*1.0936

#total /= 1.094
print("Primer Tramo: ",PrimerTramo,"Metros")
print("Segundo Tramo: ",Segundotramo,"Metros")
print("Tercer Tramo: ",Tercertramo,"Metros")
print("Total tramo: ",totalmetros,"Metros")
print("Total tramo: {:.2f}".format(totalyardas),"Yardas")









