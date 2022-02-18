#include<iostream>
#include<conio.h>
using namespace std;
float V1, V2, R;
char Opera;
int main(){
    cout<<"Primer valor: ";
    cin>>V1;
    cout<<"Segundo valor: ";
    cin>>V2;
    cout<<"Ingrese operador: ";
    cin>>Opera;
    switch(Opera){
        case('+'):R=V1+V2;break;
        case('-'):R=V1-V2;break;
        case('*'):R=V1*V2;break;
        case('/'):R=V1/V2;break;
        default:cout<<"Operador no valido";break;
    
    }
    cout<<"El resultado es: "<<R;
    return 0;
}