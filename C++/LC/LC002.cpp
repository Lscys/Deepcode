#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
char Apenom[50];//C
string nombre;//C++ 20
int Horas;
float Precio, Sueldo, Dscto, Neto;
int main(){
	cout<<"Apellidos y Nombre: ";
	cin>>nombre>>Apenom;
	cout<<"Numero de horas laboradas: ";
	cin>>Horas;
	cout<<"Precio por horas laboradas: ";
	cin>>Precio;
	Sueldo=Horas*Precio;
	Dscto=Sueldo*0.12;
	Neto=Sueldo-Dscto;
	cout<<"El sueldo basico es: "<<Sueldo<<"\n";
	cout<<"El descuento de ley es: "<<Dscto<<"\n"; 	
	cout<<"El neto a pagar es: "<<Neto;   				
	return 0;
	
}

