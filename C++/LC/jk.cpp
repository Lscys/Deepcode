#include<iostream>
#include<string.h>
using namespace std;
string Planeta[9]{"Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Pluton"};
string Mar;

int Num;
int main (){
    cout<<"Ingrese en numero del planeta: ";
    cin>>Num;
    if(Num>=1&&Num<10){
        cout<<"El planeta que eligio es: "<<Planeta[Num-1];
    }else{
        cout<<"Fuera de alcanze";
    }
    return 0;
}