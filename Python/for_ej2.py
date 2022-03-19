import string

texto_usuario = input("Introduzca un texto: ")
letra_mayusculas = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letra_mayusculas += 1

print("Las mayusculas son : {}".format(letra_mayusculas