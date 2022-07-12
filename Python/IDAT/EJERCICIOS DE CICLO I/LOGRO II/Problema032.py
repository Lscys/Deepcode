edad = int(input("Ingrese edad: "))

if edad < 15:
    print("Eres bastante joven")
elif edad < 30:
    print("Eres muy joven")
elif edad < 50:
    print("Eres joven")
elif edad < 80:
    print("Eres casi un joven")
else:
    print("Igual ya te vas haciendo mayor")