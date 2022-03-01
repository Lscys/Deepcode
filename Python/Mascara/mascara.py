import serial
import time
from tkinter import*
color="#00878F"

arduino=serial.Serial('COM2',9600)
time.sleep(2)

def foco1():
	arduino.write('a'.encode())

def foco2():
	arduino.write('s'.encode())

def foco3():
	arduino.write('d'.encode())		
	
def foco4():
	arduino.write('f'.encode())

def foco5():
	arduino.write('g'.encode())

def foco6():
	arduino.write('h'.encode())

def foco7():
	arduino.write('j'.encode())

def foco8():
	arduino.write('k'.encode())

def foco9():
	arduino.write('l'.encode())

def foco10():
	arduino.write('q'.encode())

def cerrar():
	arduino.close()
	ventana.destroy()



ventana=Tk()
Label(ventana,text="PRO-PYTHON",bg=color,fg=("#FFFFFF"),font=("Times New Roman",12)).place(x=150,y=10)
ventana.configure(background=color)
ventana.title("Casa Domotica con Arduino")
ox,oy=ventana.winfo_screenwidth()/2,ventana.winfo_screenheight()/2
ventana.geometry("400x500+%d+%d"% (ox-200,oy-100))
ventana.wm_deiconify()
ventana.iconbitmap("jk.ico")

b1=Button(ventana,text="Prende/Apaga FOCO1",font=("Comic Sans MS",10),command=foco1,bg='#C9DB2C')
b1.place(x=140,y=40)
b2=Button(ventana,text="Prende/Apaga FOCO2",font=("Comic Sans MS",10),command=foco2,bg='#C9DB2C')
b2.place(x=140,y=80)
b3=Button(ventana,text="Prende/Apaga FOCO3",font=("Comic Sans MS",10),command=foco3,bg='#C9DB2C')
b3.place(x=140,y=120)
b4=Button(ventana,text="Prende/Apaga FOCO4",font=("Comic Sans MS",10),command=foco4,bg='#C9DB2C')
b4.place(x=140,y=160)
b5=Button(ventana,text="Prende/Apaga FOCO5",font=("Comic Sans MS",10),command=foco5,bg='#C9DB2C')
b5.place(x=140,y=200)
b6=Button(ventana,text="Prende/Apaga FOCO6",font=("Comic Sans MS",10),command=foco6,bg='#C9DB2C')
b6.place(x=140,y=240)
b7=Button(ventana,text="Prende/Apaga FOCO7",font=("Comic Sans MS",10),command=foco7,bg='#C9DB2C')
b7.place(x=140,y=280)
b8=Button(ventana,text="Prende/Apaga FOCO8",font=("Comic Sans MS",10),command=foco8,bg='#C9DB2C')
b8.place(x=140,y=320)
b9=Button(ventana,text="Prende/Apaga FOCO9",font=("Comic Sans MS",10),command=foco9,bg='#C9DB2C')
b9.place(x=140,y=360)
b10=Button(ventana,text="Prende/Apaga FOCO10",font=("Comic Sans MS",10),command=foco10,bg='#C9DB2C')
b10.place(x=140,y=400)

b11=Button(ventana,text="Cerrar",font=("Comic Sans MS",10),command=cerrar,bg='#FAED1F')
b11.place(x=190,y=440)
ventana.mainloop()