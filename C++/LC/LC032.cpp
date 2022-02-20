#include<iostream>
#include<conio.h>
using namespace std;
float Ht, Tn, He, Sbasico, Bonif, Sbruto, Dscto, Sneto;
char codigo[25];
int N, Num;
int main(){
    cout<<"Numero de obreros: ",
    cin>>N;
    for(Num=1; Num<=N; Num++){
        cout<<"Codigo: ";
        cin>>codigo;
        cout<<"Horas trabajadas: ";
        cin>>Ht;
        cout<<"Tarifa x hora: ";
        cin>>Tn;
        cout<<"Horas extras: "; 
        cin>>He;
        Sbasico=Ht*Tn+He*(Tn*1.5);
        Bonif=Sbasico*0.2;
        Sbruto=Sbasico+Bonif;
        Dscto=Sbruto*0.07;
        Sneto=Sbruto-Dscto;
        cout<<"Codigo: "<<codigo<<"\n";
        cout<<"Sueldo basico: "<<Sbasico<<"\n";
        cout<<"Bonificación: "<<Bonif<<"\n";
        cout<<"Sueldo bruto: "<<Sbruto<<"\n";
        cout<<"Descuento: "<<Dscto<<"\n";
        cout<<"Sueldo neto: "<<Sneto<<"n";
    }
    return 0;
}