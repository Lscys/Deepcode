#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
string Codigo;
char Rp;
int Unidad;
float Precio, TotArt, TotGen;
int main(){
    TotGen=0;
    Rp='S';
    while(Rp=='S'){
        cout<<"Codigo del articulo: ";
        cin>>Codigo;
        cout<<"Precio unitario: ";
        cin>>Precio;
        cout<<"Numero de unidades: ";
        cin>>Unidad;
        TotArt=Precio*Unidad;
        TotGen=TotGen+TotArt;
        cout<<"Registrar otra compra (S/N): ";
        cin>>Rp;
    }
    cout<<"Total general de la compra: "<<TotGen;
    return 0;
}
