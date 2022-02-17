#include<iostream>
#include<conio.h>
using namespace std;
char Alumno[25], Curso[25];
float Practica, Parcial, Final, Promedio;
int main(){
	cout<<"Identificacion del alumno: ";
	cin>>Alumno;
	cout<<"Nombre del curso: ";
	cin>>Curso;
	cout<<"Promedio de practicas: ";
	cin>>Practica;
	cout<<"Examen parcial: ";
	cin>>Parcial;
	cout<<"Examen final: ";
	cin>>Final;
	Promedio=((Practica*2)+(Parcial*1)+(Final*3))/6;
	cout<<"Promedio final es: "<<Promedio;
	return 0;
}
