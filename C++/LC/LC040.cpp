#include<iostream>
#include<conio.h>
#include<stdlib.h>
using namespace std;
int Nro[5], S;
float Sueldo, Prom; 
int main(){
    //limpiar pantalla
    system("cls");
    for(S=0; S<=4; S++){
        cout<<"Ingrese Sueldo: ";
        cin>>Nro[S];
        Sueldo+=Nro[S];
    }
    /*for(S=0; S<=4; S++){
        cout<<Nro[S]<<"\n";
    }*/
    Prom=Sueldo/5;
    cout<<"El sueldo total es: "<<Sueldo<<endl;
    cout<<"El promedio de sueldo es: "<<Prom<<endl;
    return 0;
}
