#include<iostream>
#include<conio.h>
using namespace std;
int Nro[4];
float S, Sueldo, Prom; 
int main(){
    for(S=0; S<=4; S++){
        cout<<"Ingrese Sueldo: ";
        cin>>Nro['S'];
        Sueldo+=Nro['S'];
    }
    for(S=0; S<=4; S++){
        cout<<Nro['S'];
    }
    Prom=Sueldo/5;
    cout<<"\n El sueldo total es: "<<Sueldo<<endl;
    cout<<"El promedio de sueldo es: "<<Prom;
    return 0;
}
