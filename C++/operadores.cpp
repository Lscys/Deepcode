#include<iostream>
#include<conio.h>
using namespace std;
float monto, porcentaje=0.18, igv, total;
void Banner1(){
    cout<<"Este es mi segundo gran proyecto \n";
}
int main(){
    Banner1();
    cout<<"Ingrese su monto: ";
    cin>>monto;
    igv =monto*porcentaje;
    total =monto+igv;
    cout<<"Su IGV es: "<<igv<<"\n";
    cout<<"Su monto es: "<<total;
    return 0;
}
