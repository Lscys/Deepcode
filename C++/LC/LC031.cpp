#include<iostream>
#include<conio.h>
using namespace std;
float Suma, Promedio, Nota, Nmin, Nmax, Nnotas=10;
int i;
int main(){
    Nmax=0;
    Nmin=20;
    for(i=1; i<=Nnotas; i++){  
    cout<<"Ingrese Nota: ";
    cin>>Nota;
    if(Nota>Nmax){
        Nmax=Nota;
    }if(Nota<Nmin){
        Nmin=Nota;
    }
    Suma=Suma+Nota;
    }
    Promedio=Suma/Nnotas;
    cout<<"Maxima nota: "<<Nmax<<"\n";
    cout<<"Minima nota: "<<Nmin<<"\n";
    cout<<"Promedio: "<<Promedio;
    return 0;
}