#include<iostream>
#include<conio.h>
using namespace std;
char MM[25];
int DD, AAAA;
int main(){
    cout<<"Ingrese la fecha: ";
    cin>>DD;
    cout<<"Ingrese el Mes: ";
    cin>>MM;
    cout<<"Ingrese el ciclo: ";
    cin>>AAAA;
    cout<<"La fecha ingresada es: "<<DD<<"/"<<MM<<"/"<<AAAA;
    return 0;
}