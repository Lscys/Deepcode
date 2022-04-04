#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
using namespace std;
int posistivo, negativo;
string valotario[4], preguntas[4]{
    "1.Que significa la palabra *TOUCH*: \n\nA) Tocar B) Abrir C) Encender D) Bajar",
    "2.Que significa la palabra *MKDIR*: \n\nA) Hacer carpeta B) Entrar a carpeta C) Hacer numeros D) Mostrar codigo",
    "3.Que significa la palabra *PUSH*: \n\nA) Fuerza B) Empujar C) Aturdir D) Dar animo"
    }, Rpt[4]{
        "a", "a", "b"
    };

int main(){
    for (int i = 1; i < 4; i++)
    {
     system("cls");
     cout<<preguntas[i-1]<<"\n\n"<<"--> ";
     cin>>valotario[i-1];
     if (valotario[i-1]==Rpt[i-1])
     {
         posistivo++;
     }else{
         negativo++;
     }
     
    }
    
    for (int i = 1; i < 4; i++)
    {
     
     cout<<valotario[i-1]<<"\n";
    }
    cout<<"Las correctas son: "<<posistivo<<" Las incorrectas son: "<<negativo<<"\n";
   
    
    
}