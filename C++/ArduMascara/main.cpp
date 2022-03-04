#include <iostream>
#include "SerialClass.h"
#include<stdlib.h>
#include<ctime>
using namespace std;

int menu();
void led01();
void led02();
void led03();
void led04();
void led05();
void led06();
void led07();
void led08();
void led09();
void led10();
void delay(int segundos);//Funciona Argumentativa
Serial* Arduino = new Serial("COM4");

int main(){
	int opcion;
	while(opcion != 11){
	system("cls");
		opcion = menu();
		
		switch (opcion){
			case 1: led01();
			break;
			case 2: led02();
			break;
			case 3: led03();
			break;
			case 4: led04();
			break;
			case 5: led05();
			break;
			case 6: led06();
			break;
			case 7: led07();
			break;
			case 8: led08();
			break;	
			case 9: led09();
			break;
			case 10: led10();
			break;
			case 11: cout<<"Hasta pronto"<<endl;
			break;
			
		}
	}
}

int menu(){
	int op;
	string opciones[] = {
	"Encender led01",
	"Encender led02",
	"Encender led03",
	"Encender led04",
	"Encender led05",
	"Encender led06",
	"Encender led07",
	"Encender led08",
	"Encender led09",
	"Encender led10", 
	"Salir del programa"};
	
	cout<<"--------------------MENU-----------------------"<<endl;
	cout<<"--    1.- " + opciones[0]<<endl;
	cout<<"--    2.- " + opciones[1]<<endl;
	cout<<"--    3.- " + opciones[2]<<endl;
	cout<<"--    4.- " + opciones[3]<<endl;
	cout<<"--    5.- " + opciones[4]<<endl;
	cout<<"--    6.- " + opciones[5]<<endl;
	cout<<"--    7.- " + opciones[6]<<endl;
	cout<<"--    8.- " + opciones[7]<<endl;
	cout<<"--    9.- " + opciones[8]<<endl;
	cout<<"--    10.- " + opciones[9]<<endl;
	cout<<"--    11.- " + opciones[10]<<endl;
	cout<<"-----------------------------------------------"<<endl;
	cout<<"--    Elije una opcion: ";
	cin>>op;
	cout<<"\n\tUD. ha elejido "+ opciones[op-1]+ "\n"<<endl;
	delay(1);
	return op;
}
void led01(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("a",sizeof("a")-1);
}
void led02(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("s",sizeof("s")-1);
}
void led03(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("d",sizeof("d")-1);
}
void led04(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("f",sizeof("f")-1);
}
void led05(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("g",sizeof("g")-1);
}
void led06(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("h",sizeof("h")-1);
}
void led07(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("j",sizeof("j")-1);
}
void led08(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("k",sizeof("k")-1);
}
void led09(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("l",sizeof("l")-1);
}
void led10(){
	if(Arduino -> IsConnected())
		Arduino -> WriteData("q",sizeof("q")-1);
}

void delay(int secs){
    for(int i=(time(NULL) + secs); time(NULL)!= i; time(NULL));
}
 

