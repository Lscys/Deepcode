#include<iostream>
#include<conio.h>
#include<cstdlib>
#include<string.h>
#include<fstream>
using namespace std;
int main(){
    float pag, IGV, precio_pagar;
    int Pm, CPU, RAM, DD, TV, Case, Monitor, UO, TM, Estabilizador, precio_final, otros_final; 
    system("cls");
    cout<<"tipo de cambio de pagina: ";
    cin>>pag;
    cout<<"Placa madre: ";
    cin>>Pm;
    cout<<"Procesador 'CPU': ";
    cin>>CPU;
    cout<<"Memoria 'RAM': ";
    cin>>RAM;
    cout<<"Disco Duro: ";
    cin>>DD;
    cout<<"Tarjeta de video: ";
    cin>>TV;
    cout<<"Case: ";
    cin>>Case;
    cout<<"Monitor: ";
    cin>>Monitor;
    cout<<"Otros \n";
    cout<<"-Unidad Optica: ";
    cin>>UO;
    cout<<"-Teclado / Mouse: ";
    cin>>TM;
    cout<<"-Estabilizador: ";
    cin>>Estabilizador;
    Pm*=3.7;
    CPU*=3.7;
    RAM*=3.7;
    DD*=3.7;
    TV*=3.7;
    Case*=3.7;
    Monitor*=3.7;
    UO*=3.7;
    TM*=3.7;
    otros_final=UO+TM+Estabilizador;
    IGV=0.18;
    Estabilizador*=pag;
    precio_final=(Pm+CPU+RAM+DD+TV+Case+Monitor+UO+TM+Estabilizador);
    precio_pagar=precio_final+IGV;
    cout<<"El precio en soles sin IGV es: "<<precio_final<<endl;
    ofstream archivo;
    archivo.open("factura.txt");
    archivo<<"=============================================="<<endl;
    archivo<<"              Factura / boleta"<<endl;
    archivo<<"=============================================="<<endl;
    archivo<<"Placa madre:______________________________S/."<<Pm<<endl;
    archivo<<"Procesador CPU:___________________________S/."<<CPU<<endl;
    archivo<<"Memoria RAM:______________________________S/."<<RAM<<endl;
    archivo<<"Disco Duro:_______________________________S/."<<DD<<endl;
    archivo<<"Tarjeta de video:_________________________S/."<<TV<<endl;
    archivo<<"Case:_____________________________________S/."<<Case<<endl;
    archivo<<"Monitor:__________________________________S/."<<Monitor<<endl;
    archivo<<"Otros:____________________________________S/."<<otros_final<<endl;
    archivo<<endl;
    archivo<<"El precio en soles sin IGV es:___________S/."<<precio_final<<endl;
    archivo<<"IGV:_____________________________________S/."<<IGV<<endl;
    archivo<<"Total a pagar:___________________________S/."<<precio_pagar<<endl;
    archivo<<"\n En caso de ir a comprar a tienda, se espera el deposito \n de S/.168.66 a cuenta 191-27621568-0-72 ahorro \n soles BCP o 292-3056979545 ahorro soles INTERBANK y mandar sms de \n confirmacion 987412813"<<endl;
    archivo.close();
    system("Start factura.txt");
    getch();
    return 0;
}