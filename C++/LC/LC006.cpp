#include<iostream>
#include<conio.h>
using namespace std;
float D, T, V;
int main(){
	cout<<"Ingresar distancia: ";
	cin>>D;
	cout<<"Ingresar tiempo: ";
	cin>>T;
	V=D/T;
	cout<<"La valocidad es: "<<V<<"Km/hr";
	return 0;
}
