def mayor(n1, n2):
    if n1 > n2:
        resultado=n1
    else:
        resultado=n2
    return resultado

a = 5 
b = 12
print("El mayor valor es: "+str(mayor(a,b)))
a=25
b=12
print("El mayor valor es: "+str(mayor(a,b)))