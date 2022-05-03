A=int(input("Ingrese un numero de tres cifras: "))
B=int(input("Ingrese el segundo numero de tres cifras : "))

c3=A%10
c2=int((A%100)/10)
c1=int((A%1000)/100)
 
d3=B%10
d2=int((B%100)/10)
d1=int((B%1000)/100)


print(str(d1)+str(c2)+str(d3)) ,print(str(c1)+str(d2)+str(c3))