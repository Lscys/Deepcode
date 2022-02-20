#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
char cod;
string cur, rp;
float pf, nota;
int n;
void entrada(){
    while((rp=="s")||(rp=="S")){
        for(n=0; n<=3; n++){  
        cout<<"Ingresar Nota: ";
        cin>>nota[n];
        pf+=nota[n];
        }
        for(n=0; n<=3; n++){
            cout<<"Las notas son: "<<nota[n];
        }
        pf=pf/4;
        cout<<"El promedio es: "<<pf<<"\n";
        cout<<"--------------------------- \n";
        cout<<"Deseas continuar [s|n]: \n";
        cin>>rp;
    }
}
int main(){
    cout<<"Ingresar Codigos: \n";
    cin>>cod;
    cout<<"Ingresar Curso: \n";
    cin>>cur;
    entrada();
    return 0;
}
