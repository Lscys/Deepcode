#include<iostream>
#include<conio.h>
using namespace std;
int Num, Digi;
int main(){
    cout<<"Ingresar un Numero: ";
    cin>>Num;
    while(Num>0){
        Digi=(Num%10);
        cout<<Digi;
        Num=(Num/10);
    }
    return 0;
}