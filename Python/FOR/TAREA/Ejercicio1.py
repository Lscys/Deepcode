#ejercicio grupal
#ejercicio 01
#REALIZE UN PROGRAMA QUE REALIZE LA TABLA DE MULTIPLICAR DEL NUMERO INGRESADO

n=int(input("ingrese un numero entero positivo:"))
if n>0:
    for i in range(1,13):
        print(n,"*",i,"=",n*i)
        
else :
    print("el numero ingresado no es positivo. intentalo otra vez ")