#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<conio.h>
using namespace std;
int main(){
    string nombre, pass, correo, web;
    int edad;
    
    //Ingresantes de Datos
    cout<<"Ingrese su nombre de usuario: "<<endl;
    cin>>nombre;
    cout<<"Ingrese su password: "<<endl;
    cin>>pass;
    cout<<"Ingrese su correo: "<<endl;
    cin>>correo;
    cout<<"Ingrese su edad: "<<endl;
    cin>>edad;
    cout<<"Ingrese su pagina web: "<<endl;
    cin>>web;
    //Imprimir el recibo
    ofstream archivo;
    archivo.open("registro.txt");
    archivo <<"Nombre de usuario: "<<nombre<<endl;
    archivo <<"Password: "<<pass<<endl;
    archivo <<"El correo es: "<<correo<<endl;
    archivo <<"Tu edad es: "<<edad<<endl;
    archivo <<"Tu pagin web: "<<web<<endl;
    archivo.close();
    getch();
    system("start registro.txt");
    return 0;
}