#include<iostream>
#include<conio.h>
using namespace std;
int Num, Nd, Z;
int main(){
    Nd=0;
    cout<<"Ingrese numero entero: ";
    cin>>Num;
    for(Z=1; Z<=Num; Z++){
        if(Num%Z==0){
            cout<<Z;
            Nd=Nd+1;
        }
    }
    if(Nd==2){
        cout<<"Numero Primo";
    }else{
        cout<<"No es Primo";
    }
    return 0;
}
