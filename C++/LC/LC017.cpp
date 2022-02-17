#include<iostream>
#include<conio.h>
using namespace std;
int A, B, C, D, Mayor;
int main(){
    cout<<"Ingresar primer valor: ";
    cin>>A;
    cout<<"Ingresar segundo valor: ";
    cin>>B;
    cout<<"Ingresar tercer valor: ";
    cin>>C;
    cout<<"Ingresar cuarto valor: ";
    cin>>D;
    Mayor=A;
    if(B>Mayor){
        Mayor=B;
    }if(C>Mayor){
        Mayor=C;
    }if(D>Mayor){
        Mayor=D;
    }
    cout<<"El mayor es: "<<Mayor;
    return 0;
}