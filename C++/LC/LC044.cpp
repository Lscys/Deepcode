#include<iostream>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
using namespace std;
string Cod, Cur;
char R;
float pp, ep, ef, pf, pg;
int Nt;
void Presenta(){
    system("cls");
    cout<<"Registro de Notas \n";
    cout<<"Secretaria Academica \n";
    cout<<"N "<<Nt<<"\n";
    cout<<"--------------------------------- \n";
    
}
void PROM(){
    cout<<"--------------------------------- \n";
    pf=(pp+ep+ef)/3;
    cout<<"El promedio Final es: "<<pf<<"\n";
    cout<<"----------------------------------- \n";
    pg=pg+pf;
    
}
void PROMG(){
    pg=pg/(Nt-1);
    cout<<"----------------------------------- \n";
    cout<<"Promedio General: "<<pg<<"\n";
    cout<<"----------------------------------- \n";
    
}
int main(){
    Presenta();
    Nt=1;
    cout<<"Desea ingresar si o no: ";
    cin>>R;
    while((R=='s')||(R=='S')){
    cout<<"Ingrese Codigo: ";
    cin>>Cod;
    cout<<"Ingrese Curso: ";
    cin>>Cur;
    cout<<"Ingrese promedio de practicas: ";
    cin>>pp;
    cout<<"Ingrese examen parcial: ";
    cin>>ep;
    cout<<"Ingrese examen final: ";
    cin>>ef;
    PROM();
    cout<<"Deseas continuar [s|n]: ";
    cin>>R;
    Nt+=1;
    }
        if(R=='n'||R=='N'){
            cout<<"Nos vemos hasta luego!!!!";
        }else{
            PROMG();
        }
    return 0;
}