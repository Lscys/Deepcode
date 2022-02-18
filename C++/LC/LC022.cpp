#include<iostream>
#include<conio.h>
using namespace std;
char Ins, Cole;
float Cuota, Dscto, Importe, PdnA=0.50, PdnB=0.40, PdnC=0.30, PdpA=0.20, PdpB=0.20, PdpC=0.15;
int main(){
    cout<<"Ingresar colegio[N|P]: ";
    cin>>Cole;
    cout<<"Ingresar institucion[A|B|C]: ";
    cin>>Ins;
    cout<<"Ingresar precio: ";
    cin>>Cuota;
    switch(Ins){
        case('A'):
        if(Cole=='N'){ 
            Dscto=Cuota*PdnA;
        }else{
            Dscto=Cuota*PdpA;
        }
        case('B'):
        if(Cole=='N'){
            Dscto=Cuota*PdnB;
        }else{
            Dscto=Cuota*PdpB;
        }
        case('C'):
        if(Cole=='N'){
            Dscto=Cuota*PdnC;
        }else{
            Dscto=Cuota*PdpC;
        }
        default:cout<<"Categotia no establecida";break;
    }
    Importe=Cuota-Dscto;
    cout<<"Importe a pagar es: "<<Importe;
    return 0;
}