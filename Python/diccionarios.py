def run():
    mi_diccionario = {
        'llave': 1,
        'llave': 2,
        'llave': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }

    # print(poblacion_paises['Bolivia']) // muestra los numero del pais indicado
    
    # for pais in poblacion_paises.keys(): // muestra todos los paises
    #     print(pais)

    # for pais in poblacion_paises.values(): // muestra la poblacion de cada paiss
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():  # muestra los paises con los numeros de habitantes
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')

if __name__ == '__main__':
    run()