#include<iostream>
#include<conio.h>
using namespace std;
float Num;
int main(){
    cout<<"Ingrese valor numerico: ";
    cin>>Num;
    if(Num>0){
        cout<<"Numero ingresado es positivo";
    }else{
        cout<<"Numero ingresado es negativo";
    }
    return 0;
}