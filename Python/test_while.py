respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("Que opcion prefieres [A|B|C]: ")

if respuesta == "A":
    print("Has escogido bien")
elif respuesta == "B":
    print("Podrias haber ejelido mejor")
elif respuesta == "C":
    print("Elegiste mal")
else:
    print("No has dado una respuesta con sentido")

# numero = 12
# while numero > 1:
#   print("Mi numero {} es mayor que 1".fortmat(numero))
#   numero += 1      Bucle infinito.
#   numero -= 1      Resta de 12 hasta el 1 
#