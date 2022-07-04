#REalizar un programa que genera la tabla de dividir del 5,6,7,8,9 y 10
tabla=range(5,11)
for t in tabla:
    for i in range(1,13):
        print(t*i,"/",t,"=",(t*i)/t)