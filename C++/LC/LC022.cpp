#include<iostream>
#include<conio.h>
using namespace std;
char Ins, Cole;
float Cuota, Dscto, Importe, PdnA=0.50, PdnB=0.40, PdnC=0.30, PdpA=0.20, PdpB=0.20, PdpC=0.15;
void precio(){//Funcion
	//Ingresante
	cout<<"Ingresar precio: ";
    cin>>Cuota;
    
	//Saliente
	Importe=Cuota-Dscto;
    cout<<"Importe a pagar es: "<<Importe;
}
   

int main(){
    cout<<"Ingresar colegio[N|P]: ";
    cin>>Cole;
    cout<<"Ingresar institucion[A|B|C]: ";
    cin>>Ins;
   
    switch(Ins){
        case('A'):
        	precio();//Anidar
        if(Cole=='N'){ 
            Dscto=Cuota*PdnA;
        }else{
            Dscto=Cuota*PdpA;
        }break;
        
        case('B'):
        	precio();
        if(Cole=='N'){
            Dscto=Cuota*PdnB;
        }else{
            Dscto=Cuota*PdpB;
        }break;
        
        case('C'):
        	precio();
        if(Cole=='N'){
            Dscto=Cuota*PdnC;
        }else{
            Dscto=Cuota*PdpC;
        }break;
        
    default: cout<<"Categoria no establecida \n";break;
    }
    
    return 0;
}
