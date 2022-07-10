

alumnos = {}
for i in range(2):
    nombre = input("Ingrese el nombre del alumno: ")
    if nombre == "":
        break
    else:
        notas = input("Ingrese las nota: ")
        alumnos[nombre]=int(notas)
print(alumnos)



