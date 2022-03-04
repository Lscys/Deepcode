#include <iostream>
#include "SerialClass.h"
#include<stdlib.h>
#include<ctime>
using namespace std;

int menu();
void amarillo();
void verde();
void azul();
void apagar();
void delay(int segundos);//Funciona Argumentativa
Serial* Arduino = new Serial("COM4");

int main(){
	int opcion;
	while(opcion != 5){
	system("cls");
		opcion = menu();
		delay(2);
		switch (opcion){
			case 1: amarillo;
			break;
			case 2: verde;
			break;
			case 3: azul;
			break;
			case 4: apagar;
			break;
			case 5: cout<<"Hasta pronto"<<endl;
			break;
		}
	}
}

int menu(){
	int op;
	string opciones[] = {
	"Encender led amarillo",
	"Encender led verde",
	"Encender led azul",
	"Apagar leds",
	"Salir del programa"};
	
	cout<<"--------------------MENU-----------------------"<<endl;
	cout<<"--    1.- " + opciones[0]<<endl;
	cout<<"--    2.- " + opciones[1]<<endl;
	cout<<"--    3.- " + opciones[2]<<endl;
	cout<<"--    4.- " + opciones[3]<<endl;
	cout<<"--    5.- " + opciones[4]<<endl;
	cout<<"-----------------------------------------------"<<endl;
	cout<<"--    Elije una opcion: ";
	cin>>op;
	cout<<"\n\tUD. ha elejido "+ opciones[op-1]+ "\n"<<endl;
	return op;
}
void amarillo(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("a",sizeof("a")-1);
}
void verde(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("s",sizeof("s")-1);
}
void azul(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("d",sizeof("d")-1);
}
void apagar(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("f",sizeof("f")-1);
}

void delay(int secs){
    for(int i=(time(NULL) + secs); time(NULL)!= i; time(NULL));
}
 

