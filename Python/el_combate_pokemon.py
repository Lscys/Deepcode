from random import randint

vida_pikachu = 100
vida_squirtle = 100

while vida_pikachu > 0 and vida_squirtle > 0 :
    # se desenvuelven los turnos de combate

    # turno de pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))

    input("Enter para poder continuar...\n\n")

    # Turno de Squirtle 
    print("Turno de Squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("¿Que ataque deseas realizar? [P]lacaje, [A]Pistola de agua, [B]Burbuja: ")

    if ataque_squirtle == "P":
        print("Squirtle atace con Placaje")
        vida_pikachu -= 20
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de agua")
        vida_pikachu -= 18
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 15

    print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))
    input("Enter para poder continuar...\n\n")

if vida_pikachu > vida_squirtle:
    print("Gano Pikachu")
    exit()
else:
    print("Gano Squirtle")
    exit()