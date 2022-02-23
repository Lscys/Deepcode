//Programacion Estructurada
//Programacion Orientado a Objetos
//Programacion Modular
#include<iostream>
#include<conio.h>
#include<cstdlib>
#include<string.h>
#include<fstream>
using namespace std;

string menbrete = "\n En caso de ir a comprar a tienda, se espera el deposito \n de S/.168.66 a cuenta 191-27621568-0-72 ahorro \n soles BCP o 292-3056979545 ahorro soles INTERBANK y mandar sms de \n confirmacion 987412813\n By: Lscys";

int main(){
    float Tcambio, IGV, precio_pagar, porcentaje=0.18;
    int Pm, CPU, RAM, DD, TV, Case, Monitor, UO, TM, Estabilizador, Subtotal, otros_final; 
    system("cls");//Limpiar pantalla
    //Ingresantes
    cout<<"tipo de cambio: \tS/.";
    cin>>Tcambio; //3.7
    cout<<"\nPlaca madre: \t\t$";
    cin>>Pm;
    cout<<"Procesador 'CPU': \t$";
    cin>>CPU;
    cout<<"Memoria 'RAM': \t\t$";
    cin>>RAM;
    cout<<"Disco Duro: \t\t$";
    cin>>DD;
    cout<<"Tarjeta de video: \t$";
    cin>>TV;
    cout<<"Case: \t\t\t$";
    cin>>Case;
    cout<<"Monitor: \t\t$";
    cin>>Monitor;
    cout<<"Otros \n";
    cout<<"-Unidad Optica: \t$";
    cin>>UO;
    cout<<"-Teclado / Mouse: \t$";
    cin>>TM;
    cout<<"-Estabilizador: \t$";
    cin>>Estabilizador;

    //Calculos
    otros_final=UO+TM+Estabilizador;
    Subtotal=(Pm+CPU+RAM+DD+TV+Case+Monitor+UO+TM+Estabilizador);
    precio_pagar = Subtotal*IGV;
    IGV=Subtotal*porcentaje;
    precio_pagar=Subtotal+IGV;
    //Saliente Final
    cout<<"El precio sin IGV es: \t$"<<Subtotal<<"(S/."<<Subtotal*Tcambio<<")"<<"\n"<<endl;
    cout<<"Presione una tecla para mostrar su factura --> ";
    getch();
    ofstream archivo;
    archivo.open("factura.txt");
    archivo<<"=============================================="<<endl;
    archivo<<"              Factura / boleta"<<endl;
    archivo<<"=============================================="<<endl;
    archivo<<"Placa madre:______________________________"<<"$"<<Pm<<" (S/."<<Pm*Tcambio<<")"<<endl;
    archivo<<"Procesador CPU:___________________________"<<"$"<<CPU<<"(S/."<<CPU*Tcambio<<")"<<endl;
    archivo<<"Memoria RAM:______________________________"<<"$"<<RAM<<"(S/."<<RAM*Tcambio<<")"<<endl;
    archivo<<"Disco Duro:_______________________________"<<"$"<<DD<<"(S/."<<DD*Tcambio<<")"<<endl;
    archivo<<"Tarjeta de video:_________________________"<<"$"<<TV<<"(S/."<<TV*Tcambio<<")"<<endl;
    archivo<<"Case:_____________________________________"<<"$"<<Case<<"(S/."<<Case*Tcambio<<")"<<endl;
    archivo<<"Monitor:__________________________________"<<"$"<<Monitor<<"(S/."<<Monitor*Tcambio<<")"<<endl;
    archivo<<"Otros:____________________________________"<<"$"<<otros_final<<"(S/."<<otros_final*Tcambio<<")"<<endl;
    archivo<<endl;
    archivo<<"El precio en soles sin IGV es:___________"<<"$"<<Subtotal<<"(S/."<<Subtotal*Tcambio<<")"<<endl;
    archivo<<"IGV:_____________________________________"<<"$"<<IGV<<"(S/."<<IGV*Tcambio<<")"<<endl;
    archivo<<"Total a pagar:___________________________"<<"$"<<precio_pagar<<"(S/."<<precio_pagar*Tcambio<<")"<<endl;
    archivo<<menbrete;
    archivo.close();
    system("Start factura.txt");
    
    return 0;
}