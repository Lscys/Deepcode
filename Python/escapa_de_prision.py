import random
from re import A

menu = """
Han logrado escapar de la carcel, tu amigo y tu
ahora necesitan salir de la prision, pero para poder
salir tienen que ir al fondo del pazillo donde se encuentra
un monstruo que tapa la salida, pero tambien hay una puerto 
semi abierta y una escotilla en el suelo donde puede saltar:
     
     1 - Voy por la puerte semi abierta
     2 - Voy por la escotilla 

Elija una opcion: """

opcion = int(input(menu))
if opcion == 1:
    numero_random_rata = random.randint(1, 100)
    print("Te encontrastes con una rata gigante que te \nhace una pregunta para poder pasar \npero si no aceptas te devorara")
    print("Cuanto es 13 * {}".format(numero_random_rata))
    resultado = int(input("Dime la respuesta: "))
    if resultado ==  13 * numero_random_rata:
        print("La rata te dejara pasar por tener un intelectual alto")
    else:
        print("Te matara por no saber algo tan facil")
elif opcion == 2:
    AoB = input("Bajaste por la escotilla y te encontrastes dos puertes mas\n hay una cartel que dice\n que una de las puertes de matara y otra te llevara fuera de la carcel [A/B]")
    if AoB == "A":
        print("Moriras por una caida muy alta")
    else:
        print("Escogiste la puerta correcta y sales de la carcel")
else:
    print("No escogiste ni una de las opciones")