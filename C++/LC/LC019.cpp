#include<iostream>
#include<conio.h>
using namespace std;
int Dia;
int main(){
    cout<<"Ingrese el numero del dia: ";
    cin>>Dia;
    switch(Dia){
        case(1):cout<<"El dia domingo";break;
        case(2):cout<<"El dia Lunes";break;
        case(3):cout<<"El dia Martes";break;
        case(4):cout<<"El dia Miercoles";break;
        case(5):cout<<"El dia Jueves";break;
        case(6):cout<<"El dia Viernes";break;
        case(7):cout<<"El dia Sabado";break;
        default:cout<<"El valor ingresado no es correcto";
    }
    return 0;
}