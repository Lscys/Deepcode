#include<iostream>
#include<conio.h>
#include<windows.h>
using namespace std;
char Nom[100];
int numero;
int main(){
    cout<<"Ingrese apellidos y nombres: ";
    cin>>Nom;
    for(int numero=1; numero<=10; numero++){
        cout<<Nom<<endl;
    }
    return 0;
  }