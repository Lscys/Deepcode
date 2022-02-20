#include<iostream>
#include<conio.h>
using namespace std;
int Codigo, Cantidad;
float Precio, Importe;
int main(){
    cout<<"Computo de inventario \n";
    cout<<"------------------------- \n";
    cout<<"Para terminar digitar -999 \n";
    cout<<"------------------------- \n";
    while(Codigo!=-999){
        cout<<"Seleccione el departamento \n";
        cout<<"Cual es el  siguiente codigo del producto: ";
        cin>>Codigo;
        if(Codigo==-999){
            break;
        }    
        cout<<"Cuantas unidades se compraron: ";
        cin>>Cantidad;
        cout<<"Cual es el precio unitario del articulo: ";
        cin>>Precio;
        cout<<Cantidad<<" unidades de # "<<Codigo<<" representa "<<Precio;
    }
    cout<<"Fin del computo";
    return 0;
}