#include<iostream>
#include<conio.h>
using namespace std;
float C, Dscto, Impuesto, Importe, Pdscto=0.20, Pimpto=0.15;
int main(){
    cout<<"Ingresar consumo: ";
    cin>>C;
    if(C>30){
        Dscto=C*Pdscto;
    }else{
        Dscto=0;
    }
    Impuesto=(C-Dscto)*Pimpto;
    Importe=C-Dscto+Impuesto;
    cout<<"Consumo:"<<C<<"\n";
    cout<<"Descuento: "<<Dscto<<"\n";
    cout<<"Impuesto: "<<Impuesto<<"\n";
    cout<<"Importe a pagar: "<<Importe;
    return 0;
}