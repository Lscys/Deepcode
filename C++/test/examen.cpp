#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
using namespace std;
int posistivo, negativo;
string calificacion[4],valotario[4], preguntas[4]{
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
         calificacion[i-1]="Aprobado\t\t";
         posistivo++;
         
     }else{         
         negativo++;
         calificacion[i-1]="Desaprobado\t";
     }
     
    }
    
    
    cout<<"Las correctas son: "<<posistivo<<" Las incorrectas son: "<<negativo<<"\n\n";
    cout<<"Presione una tecla para ver sus resultados\n";
    getch();
    ofstream archivo;
    archivo.open("examen.txt");
    archivo<<"============================================================"<<endl;
    archivo<<"=                   Examen de Programacion                 ="<<endl;
    archivo<<"============================================================\n"<<endl;
    for (int i = 1; i < 4; i++)
    {     
     archivo<<"La respuesta "<<i<<" es: "<<valotario[i-1]<<" "<<calificacion[i-1]<<"||"<<" El correcto es: "<<Rpt[i-1]<<"\n";
    }
    archivo.close();
    system("Start examen.txt");
   
    
    
}