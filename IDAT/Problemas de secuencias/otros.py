def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


segundos = [10, 100, 40, 1500, 6000, 60, 59, 100000]
for cantidad_segundos in segundos:
    convertido = segundos_a_segundos_minutos_y_horas(cantidad_segundos)
    print(f"Los {cantidad_segundos} segundos se convierten a {convertido}")
