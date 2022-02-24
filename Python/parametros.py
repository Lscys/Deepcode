def conversación(mensaje):
    print('Hola')
    print('Como estas')
    print(mensaje)
    print('Adios')

opcion = int(input('Eliga una opcion(1, 2, 3): '))
if opcion == 1:
    conversación('Elejiste la opcion 1')
elif opcion == 2:
    conversación('Elejiste la opcion 2')
elif opcion == 3:
    conversación('Elejiste la opcion 3')
else:
    print('Elija una opcion correcta porfavor')

