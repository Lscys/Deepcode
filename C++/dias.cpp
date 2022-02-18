#include<iostream>
#include<conio.h>
using namespace std;
int dia;
int main(){
    cout<<"Ingrese el numero de dia: ";
    cin>>dia;
    switch(dia){
        case 1: cout<<"El dia es domingo";break;
        case 2: cout<<"El dia es lunes";break;
        case 3: cout<<"El dia es martes";break;
        case 4: cout<<"El dia es miercoles";break;
        case 5: cout<<"El dia es jueves";break;
        case 6: cout<<"El dia es viernes";break;
        case 7: cout<<"El dia es sabado";break;
        default: cout<<"El valor ingresado no es correcto";
        
    }

    return 0;
}