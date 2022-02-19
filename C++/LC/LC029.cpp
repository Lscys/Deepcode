#include<iostream>
#include<conio.h>
using namespace std;
float N, Fac, C;
int main(){
    cout<<"Ingrese Valor Numerico: ";
    cin>>N;
    Fac=1;
    for(C=1; C<=N; C++){
        Fac=Fac*C;
    }
    cout<<"Factorial de N es: "<<Fac;

    return 0;
}