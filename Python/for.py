# RECORRER UNA LISTA Y EJECUTAR UN CODIGO PARA CADA ITEM QUE ESTA EN LA LISTA
vocales = ["a", "e", "i", "o", "u"]
frase = "Hola, hoy estoy aprendiendo Python"
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        print("He encontrado una '{}'".format(letra))
        vocales_encontradas +=1

print("Vocales encontradas: {}".format(vocales_encontradas))



# ESTO REPITE ALGO UN SUERTO DED VECES SEGUN EL RANGO
# numero_de_repeticiones = int(input("Cuantas veces quieres repetir el mensaje?"))
# for a in range(numero_de_repeticiones):
    # print(a)