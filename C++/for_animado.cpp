#include<iostream>
#include<conio.h>
#include<windows.h>//Sleep Dormir(tiempo de retardo)
using namespace std;
int numero, i;
void iteracion(){
    for( i=1; i<=numero; i++){
        cout<<i<<endl;
        Sleep(1000);
    }
    for(i=numero-1; i>=1; i--){
        cout<<i<<endl;
        Sleep(1000);
    }
}
int main(){
    cout<<"Ingrese un numero: ";
    cin>>numero;
    iteracion();
    getch();
    return 0;
}