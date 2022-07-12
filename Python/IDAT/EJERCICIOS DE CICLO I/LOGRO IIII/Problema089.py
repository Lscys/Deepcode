# .key()
dct={"cat":"chat", "dog":"chien", "horse":"cheval"}
for key in dct.keys():
    print(key, "-->", dct[key])

print(" ")
# .items() 
dct={"cat":"chat", "dog":"chien", "horse":"cheval"}
for clave, valor in dct.items():
    print(clave, "-->",valor)

print(" ")
# .values()
dct={"cat":"chat", "dog":"chien", "horse":"cheval"}
for valor in dct.values():
    print(valor)

print(" ")
# Agregar al diccionario
dct={"cat":"chat", "dog":"chien", "horse":"cheval"}
dct["lion"]="lion"
print(dct)

print(" ")
# Cambiar 
dct={"cat":"chat", "dog":"chien", "horse":"cheval"}
dct["cat"]="lion"
print(dct)

print(" ")
# Quitar del diccionario
dct={"cat":"chat", "dog":"chien", "horse":"cheval"}
del dct["dog"]
print(dct)
