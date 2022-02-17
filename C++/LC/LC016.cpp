#include<iostream>
#include<conio.h>
using namespace std;
float C, Dscto, Impuesto, Importe, Pdscto1=0.30, Pdscto2=0.20, Pdscto3=0.15, Pdscto4=0.10, Pimpto=0.15; 
int main(){
    cout<<"Ingresar consumo: ";
    cin>>C;
    if(C>100){
        Dscto=C*Pdscto1;
    }else{
        if(C>60){
            Dscto=C*Pdscto2;
        }else{
            if(C>30){
                Dscto=C*Pdscto3;
            }else{
                Dscto=C*Pdscto4;
            }
        }
    }
    Impuesto=(C-Dscto)*Pimpto;
    Importe=C-Dscto+Impuesto;
    cout<<"Consumo: "<<C<<"\n";
    cout<<"Descuento: "<<Dscto<<"\n";
    cout<<"Impuesto: "<<Impuesto<<"\n";
    cout<<"Importe a pagar: "<<Importe;
    return 0;
}