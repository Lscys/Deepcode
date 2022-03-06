titulo = "Bienvenido al test sobre el Flan"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: Que haces cuando ves un baso de flan?\n"
               "A - Salgo corriendo\n"
               "B - Pruebo unos de los Flanes o incluso varios\n"
               "C - No puedo evitar devorarlo\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones disponibles son A, B y C")
    exit()

opcion = input("Pregunta 2: Como prefieres el flan?\n"
               "A - Ni lo miro cuando lo veo\n"
               "B - Lo compro hecho solo para comer\n"
               "C - Lo haces en casa y es mucho mas refrescante\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones disponibles son A, B y C")
    exit()

opcion = input("Pregunta 3: Te gusta o eres un fanatico del flan?\n"
               "A - No me gusta\n"
               "B - Me  gusta el flan\n"
               "C - Soy una fanatico del flan\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones disponibles son A, B y C")
    exit()

if puntuacion >= 25:
    print("Resultado: Felicidades, eres un fanatico del Flan")
elif puntuacion >= 15:
    print("Resultado: Felicidades, eres una persona que le gusta el Flan")
else:
    print("Resultado: Felicidades, no te gusta el Flan")