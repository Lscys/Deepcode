"""
Consideramos un programa que pide un valor y nos dice
-Si es múltiplo de dos
-Si es multiplo de cuatro y dos
-Si no es multiplo de dos 
"""
numero = int(input("Escriba un numero: "))
if numero % 4 == 0:
    print("El ",numero," es multiplo de cuatro y de dos")
elif numero % 2 == 0:    
    print("El ",numero," es multiplode dos")
else:
    print("El ",numero," no es múltiplo de dos")