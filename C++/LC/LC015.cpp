#include<iostream>
#include<conio.h>
using namespace std;
float C, Dscto, Impuesto, Importe, Pdscto1=0.20, Pdscto2=0.10, Pimpto=0.15;
int main(){
    cout<<"Ingrese consumo: ";
    cin>>C;
    if(C>30){
        Dscto=C*Pdscto1;
    }else{
        Dscto=C*Pdscto2;
    }
    Impuesto=(C-Dscto)*Pimpto;
    Importe=C-Dscto+Impuesto;
    cout<<"Consumo: "<<C<<"\n";
    cout<<"Descuento: "<<Dscto<<"\n";
    cout<<"Impuesto: "<<Impuesto<<"\n";
    cout<<"Importe a pagar: "<<Importe;
    return 0;
}