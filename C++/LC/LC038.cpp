#include<iostream>
#include<conio.h>
using namespace std;
int Seleccion;
int main(){
    while((Seleccion<1)||(Seleccion>3)){
        cout<<"Selecione el departamento: \n";
        cout<<"1.Contabilidad: \n";
        cout<<"2.Ingenieria: \n";
        cout<<"3.Marketing: \n";
        cout<<"Seleccione el area: ";
        cin>>Seleccion;
    }
    switch(Seleccion){
        case(1):cout<<"Alejandro Sanz";break;
        case(2):cout<<"Britney Spears";break;
        case(3):cout<<"Bob Marley";break;
    }
    cout<<"  Identificacion correcta \n";
    return 0;
}