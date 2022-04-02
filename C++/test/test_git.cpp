#include<iostream>
#include<conio.h>
#include<string.h>

using namespace std;

string respuesta1, respuesta2, respuesta3;
int rpt, rptn;

int main() {
    cout<<"\t\tTEST DE PALABRAS  ABREBIADAS"<<endl;
    cout<<"Este programa fue hecho para ver el nivel de ingles y ver como interpretas\npalabras abreviadas en programacion, que te sera fundamental aprender.\n"<<endl;
    cout<<"Empezaremos con palabras faciles y con cada respuesta correcta se te evaluara para ver cual fue tu maxima puntuacion.\n"<<endl;
    
    cout<<"1.Que significa la palabra *TOUCH*"<<endl;
    cout<<"A).Tocar B).Abrir C).Encender D).Bajar\n";
    cin>>respuesta1;
        
    cout<<"2.Que significa la palabra *MKDIR*"<<endl;
    cout<<"A).Hacer carpeta B).Entrar a carpeta C).Hacer numeros D).Mostrar codigo\n";
    cin>>respuesta2;

    cout<<"3.Que significa la palabra *PUSH*"<<endl;
    cout<<"A).Fuerza B).Empujar C).Aturdir D).Dar animo\n";
    cin>>respuesta3;
     
    
    if (respuesta1 == "A") {
        cout<<"Respuesta 1. correcta\n";
        rpt++;
    }else{
        cout<<"Respuesta 1. incorrecta\n";
        rptn++;
    }
    if (respuesta2 == "A") {
        cout<<"Respuesta 2. correcta\n";
        rpt++;
    }else{
        cout<<"Respuesta 2. incorrecta\n";
        rptn++;
    }
    if (respuesta3 == "B") {
        cout<<"Respuesta 3. correcta\n";
        rpt++;
    }else{
        cout<<"Respuesta 3. incorrecta\n";
        rptn++;
    }

    cout<<"Las corectas son: "<<rpt<<"\n";
    cout<<"Las incorrectas son: "<<rptn;
    return 0;
}