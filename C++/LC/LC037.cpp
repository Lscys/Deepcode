#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
string Apenom, Curso;
char Rp;
float Prom, Suma, PromP;
int NCur;
int main(){
    Suma=0;
    Rp='S';
    NCur=0;
    cout<<"Hola ingrese su nombre: ";
    cin>>Apenom;
    cout<<"Desea Ingresar al curso[S/N]: ";
    cin>>Rp;
    while(Rp=='S'){
        cout<<"Nombre del curso: ";
        cin>>Curso;
        cout<<"Promedio del curso: ";
        cin>>Prom;
        Suma+=Prom;//c++ 20
        //Suma=Suma+Prom;
        //NCur=NCur+1; Acumulador
        NCur+=1;
        cout<<"Registrar otro curso (S/N): ";
        cin>>Rp;
    }
    PromP=Suma/NCur;
    cout<<Apenom<<" su promedio es: "<<PromP;
    return 0;
}