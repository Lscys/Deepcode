#include<iostream>
#include<conio.h>
using namespace std;
float Valor,Num,Resu,Valor1,Num1,Resul;

void Multiplicacion(){
    cout<<"Table del: ";
    cin>>Num1;
    for(int Valor1=1; Valor1<=12; ++Valor1){
        Resul=Valor1*Num1;
        cout<<Num1<<" x "<<Valor1<<" = "<<Resul<<endl;

    }
}
 void Suma(){
     cout<<"Table del: ";
    cin>>Num1;
    for(int Valor1=1; Valor1<=12; Valor1++){
        Resul=Valor1+Num1;
        cout<<Num1<<" + "<<Valor1<<" = "<<Resul<<endl;

    }
 }
 
 void Resta(){
     cout<<"Table del: ";
    cin>>Num1;
    for(int Valor1=1; Valor1<=12; Valor1++){
        Resul=Valor1-Num1;
        cout<<Num1<<" - "<<Valor1<<" = "<<Resul<<endl;

    }
 }

void Divicion(){
     cout<<"Table del: ";
    cin>>Num1;
    for(int Valor1=1; Valor1<=12; Valor1++){
        Resul=Valor1/Num1;
        cout<<Num1<<" / "<<Valor1<<" = "<<Resul<<endl;

    }
 }
int main(){

    while(true){
        char respuesta;
        cout<<"Ingrese la opcion de tabla: ";
        cin>>respuesta;
    if(respuesta=='s'||respuesta=='S'){
        Suma();
    }
    if(respuesta=='r'||respuesta=='R'){
        Resta();
    } 
    if(respuesta=='m'||respuesta=='M'){
        Multiplicacion();
    }
    if(respuesta=='d'||respuesta=='D'){
        Divicion();
    } 
    char StrRp;
    cout<<"Continuas S/N: ";
    cin>>StrRp;
    if(StrRp=='s'||StrRp=='S'){
        ;
    
    }else if(StrRp=='n'||StrRp=='N'){
        cout<<"Nos vemos luego";
        break;
    }else{
        cout<<"Letra equivocada. \n Continuamos."<<endl;
    }

    }
    
    return 0;
}