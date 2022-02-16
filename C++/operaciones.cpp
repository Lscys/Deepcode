#include<iostream>
#include<conio.h>
using namespace std;
//Variables globales
int /*variable del tipo entero*/ numero;
//funcion
void/*Vacio*/banner(){
    cout<<"Este es mi primer gran programa \n";
} 
int main(){
    banner();//Anidado
    cout<<"Ingrese tu edad: ";
    cin>>numero;
    if (numero>=18)
    {
       cout<<"Eres mayor de edad";
    }else{
        cout<<"Eres menor de edad";
    }
    
    getch();
    return 0;
}
