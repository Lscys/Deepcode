dct={"cat":"chat", "dog":"chien", "horse":"cheval"}
palabras = {"cat", "lion", "horse"}
for i in palabras:
    if i in dct:
        print(i, "-->", dct[i])
    else:
        print("No esta en el diccionario: ", i)