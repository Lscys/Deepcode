#include<iostream>
#include<conio.h>
using namespace std;
float monto, porcentaje=0.18, igv, total;
void Banner(){
    cout<<"Este es mi segundo gran proyecto \n";
}
int main(){
    Banner();
    cout<<"Ingrese su monto: ";
    cin>>monto;
    igv=monto*porcentaje;
    total=monto+igv;
    cout<<"Su igv es: "<<igv<<"\n";
    cout<<"Su monto es: "<<total;
    return 0;
}