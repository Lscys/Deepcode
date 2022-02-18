#include<iostream>
#include<conio.h>
using namespace std;
int H, M, S;
int main(){
    cout<<"Ingresar cantidad de segundos: ";
    cin>>S;
    H=0;
    M=0;
    if(S>=60){
        M=(S/60);
        S=(S%60);
    }if(M>=60){
        H=(M/60);
        M=(M%60);
    }
    cout<<"Horas: "<<H<<"\n";
    cout<<"Minutos: "<<M<<"\n";
    cout<<"Segundos: "<<S;
    return 0;
}