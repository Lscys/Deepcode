#include<iostream>
#include<conio.h>
using namespace std;
char Descrip[50];
int Stock;
float Precio, Ganancia, Pventa, Valoriza; 
int main(){
	cout<<"Descripcion del articulo: ";
	cin>>Descrip;
	cout<<"Precio de compra: ";
	cin>>Precio;
	cout<<"Porcentaje de ganancia: ";
	cin>>Ganancia;
	cout<<"Numero de unidades en stock: ";
	cin>>Stock;
	Pventa = Precio+Precio*(Ganancia/100);
	Valoriza = Pventa*Stock;
	cout<<"El precio de venta es: "<<Pventa<<"\n";
	cout<<"La valorizacion es: "<<Valoriza;
	return 0;
}
