#include<iostream>
#include<conio.h>
using namespace std;
char Cod[25], Arti[25];
float Prec, Venta, Monto, igv=0.18;
int Cant;
int main(){
    cout<<"Ingrese Codigo: ";
    cin>>Cod;
    cout<<"Ingrese Articulo: ";
    cin>>Arti;
    cout<<"Ingrese Precio: ";
    cin>>Prec;
    cout<<"Ingrese Cantidad: ";
    cin>>Cant;
    Venta=Prec*Cant;
    Monto=Venta+(Venta*igv);
    cout<<"El total de venta es: "<<Venta<<"\n";
    cout<<"El monto total de ventas es: "<<Monto;
    return 0;
}