total_de_alumnos = int(input("Cuantos estudiantes hay en el salon?: "))
hombre = int(input("Ingrese el numero de varones: "))
mujeres = int(input("Ingrese el numero de mujeres: "))

resultado_hombres = total_de_alumnos * hombre / 100
resultado_mujeres = total_de_alumnos * mujeres / 100

print("En el porcentaje de hombre es",resultado_hombres,)
print("En el porcentaje de mujeres es ",resultado_mujeres,)