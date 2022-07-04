
from tkinter import E

inicio = 0
i=0
s=0

while i <= 200:
    inicio+=i  
    print(inicio)   
    i+=1    
    s=s+inicio
print(f"La suma de los primeros terminos es {s}")
