#include<iostream>
#include<conio.h>
#include<cstdlib>
#include<string.h>
#include<fstream>
using namespace std;
void Banner(){
    cout<<"En caso de ir a comprar a tienda, \n se espera el deposito de S/.168.66 a cuenta 191-27621568-0-72 ahorro \n soles BCP o 292-3056979545 ahorro soles INTERBANK y mandar sms de confirmacion 987412813"<<endl;
}
int main(){
    float pag;
    int Pm, CPU, RAM, DD, TV, Case, Monitor, UO, TM, Estabilizador, precio_final; 
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
    Estabilizador*=pag;
    precio_final=(Pm+CPU+RAM+DD+TV+Case+Monitor+UO+TM+Estabilizador);
    cout<<"El precio en soles sin IGV es: "<<precio_final<<endl;
    ofstream archivo;
    archivo.open("factura.txt");
    archivo<<"=============================================="<<endl;
    archivo<<"Factura / boleta"<<endl;
    archivo<<"=============================================="<<endl;
    archivo<<"Placa madre:______________________________"<<Pm<<endl;
    archivo<<"Procesador CPU:___________________________"<<CPU<<endl;
    archivo<<"Memoria RAM:______________________________"<<RAM<<endl;
    archivo<<"Disco Duro:_______________________________"<<DD<<endl;
    archivo<<"Tarjeta de video:_________________________"<<TV<<endl;
    archivo<<"Case:_____________________________________"<<Case<<endl;
    archivo<<"Monitor:__________________________________"<<Monitor<<endl;
    archivo<<"Otros: "<<UO<<"+"<<TM<<"+"<<Estabilizador<<endl;
    archivo<<"El precio en soles sin IGV es: "<<precio_final<<endl;
    archivo<<"\n En caso de ir a comprar a tienda, se espera el deposito \n de S/.168.66 a cuenta 191-27621568-0-72 ahorro \n soles BCP o 292-3056979545 ahorro soles INTERBANK y mandar sms de \n confirmacion 987412813"<<endl;
    archivo.close();
    getch();
    system("Start factura.txt");
    return 0;
}