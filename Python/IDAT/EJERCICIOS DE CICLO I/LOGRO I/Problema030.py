"""
Consideremos un programa que pide la edad y en funcion del valor recibido da un mensaje
diferente, podemos distinguir por ejemplo:
-Si el valor en negativo, se trata de un error
-Si el valor es entre 0 y 17 se trata de un menor de edad 
.Si el valor es superior o igual a 18, se trata de un mayor de edad
"""
edad = int(input("Cuantos años tiene: "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad >= 0 and edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")