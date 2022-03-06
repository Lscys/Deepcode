opcion = input("¿[I]ios o [A]Android?: ")

movil_ideal = "ninguno"

if opcion == "A":  # Ha contestado Android
    opcion = input("¿Tienes dinero? [S/N]: ")

    if opcion == "S":  # Tiene dinero
        opcion = input("¿Te importa la camara del movil? [S/N]: ")

        if opcion == "S": # Si le importa la camara
            movil_ideal = "Google Pixel Supercamara"

        else:  # No le importa la camara
            movil_ideal = "Android calidad-precio (Xiaomi)"
        
    else:  # Si no tiene dinero
        movil_ideal = "Android Chino 100€"

elif opcion == "I":  # Ha contestado IOS
    opcion = input("¿Tienes dinero? [S/N]: ")

    if opcion == "S":  # Tiene dinero
        movil_ideal = "iPhone Ultra Pro Max"

    else:  # No tiene dinero
        movil_ideal = "iPhone segunda mano"

print("Tu movil ideal es " + movil_ideal)