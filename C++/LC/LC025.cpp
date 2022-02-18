#include<iostream>
#include<conio.h>
using namespace std;
int Num, i, Res;
int main(){
    cout<<"Ingresar numero: ";
    cin>>Num;
    for(i=0; i<=12; i++){
        Res=Num*i;
        cout<<Num<<"*"<<i<<"="<<Res<<endl;
    }
    return 0;
}