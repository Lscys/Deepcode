#include<iostream>
#include<conio.h>
using namespace std;
char Mar;
int Cant;
float Prec, Pbruto, Dscto, Importe, Pdscto1=0.10, Pdscto2=0.15, Pdscto3=0.20, Pdscto4=0.25, Pdscto5=0.30;
int main(){
    cout<<"Ingresar Marca: ";
    cin>>Mar;
    cout<<"Ingresar Cantidad: ";
    cin>>Cant;
    cout<<"Ingresar Precio: ";
    cin>>Prec;
    Pbruto=Cant*Prec;
    switch (Mar){
        case('3'):Dscto=Pbruto*Pdscto1;break;
        case('M'):Dscto=Pbruto*Pdscto2;break;
        case('D'):Dscto=Pbruto*Pdscto3;break;
        case('T'):Dscto=Pbruto*Pdscto4;break;
        case('F'):Dscto=Pbruto*Pdscto5;break;
        default:cout<<"No esta en la marca de 1-5";
    }
    Importe=Pbruto-Dscto;
    cout<<("Importe Bruto: ")<<Pbruto<<"\n";
    cout<<("Descuento: ")<<Dscto<<"\n";
    cout<<("Importe a pagar: ")<<Importe;
    return 0; 
}
