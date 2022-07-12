"""
Crear un diccionario que almacene nombre y que le corresponde sus apellidos, de 5 alumnos
Luego ingrese un nombre para que lo busque en el diccionario mostrando el nombre del 
alumno si esta en el diccionario 
"""

alumnos = {}
for i in range(2):
    nombre = input("Ingrese el nombre del alumno: ")
    apellidos = input("Ingrese los apellidos del alumno: ")
    alumnos[nombre]=apellidos
    print(alumnos)
nom = input("Ingrese el nombre del alumnos a buscar: ")
print(alumnos)
print(alumnos.get(nom))