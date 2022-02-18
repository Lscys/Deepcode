#include<iostream>
#include<conio.h>
using namespace std;
float Sueldo, Promedio, Suma;
int i;
int main(){
    for(i=1; i<=8; i++){
        cout<<"Ingrese sueldo: ";
        cin>>Sueldo;
        Suma=Suma+Sueldo;
    }
    Promedio=Suma/8;
    cout<<"La sumatoria es: "<<Suma<<"\n";
    cout<<"El promedi es: "<<Promedio;
    return 0;
}