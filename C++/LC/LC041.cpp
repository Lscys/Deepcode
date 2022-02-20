#include<iostream>
#include<string.h>
using namespace std;
string Planeta[9]{"Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Pluton"};
int Num;
int main(){ 
    cout<<"Ingresar Numero del planeta: ";
    cin>>Num;
    if((Num>0)&&(Num<10)){
        cout<<"El nombre del planeta es: "<<Planeta[Num-1];
    }else{
        cout<<"El numero no es valido";
    }
    return 0;
}