#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
char cod;
string cur, rp;
float pf, nota[4];
int n;
int main(){
    cout<<"Ingresar Codigos: ";
    cin>>rp;
    
    while((rp=="s")||(rp=="S")){
        
        for(n=0; n<4; n++){  
        cout<<"Ingresar Nota: ";
        cin>>nota[n];
        pf+=nota[n];
        }

        /*for(n=0; n<4; n++){
            cout<<"Las notas son: "<<nota[n]<<"\n";
        }*/

        pf/=4;
        cout<<"El promedio es: "<<pf<<"\n";
        cout<<"--------------------------- \n";
        cout<<"Deseas continuar [s|n]: ";
        cin>>rp;
    }
    return 0;
}
