#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
using namespace std;
int posistivo, negativo;
string calificacion[20],valotario[20], preguntas[20]{
    "1.Que significa la palabra *TOUCH*: \nA) Tocar B) Abrir C) Encender D) Bajar",
    "2.Que significa la palabra *MKDIR*: \nA) Hacer carpeta B) Entrar a carpeta C) Hacer numeros D) Mostrar codigo",
    "3.Que significa la palabra *PUSH*: \nA) Fuerza B) Empujar C) Aturdir D) Dar animo",
    "4.Que significa la palabra *PULL*: \nA).Ver B).Dar C).Atender D).Jalar",
    "5.Que significa la palabra *STAT* \nA).Numeros B).Letras C).Estadistica D).Multiplicacion",
    "6.Que significa la palabra *ADD*\nA).Adentrar B).Despojar C).Pedir D).Agregar",
    "7.Que significa la palabra *ALL*\nA).Ustedes B).Todos C).Ellos D).Aquellos",
    "8.Que significa la palabra *MAIN*\nA).Principal B).Secundario C).Octavo D).Decimo",
    "9.Que significa la palabra *CLONE*\nA).Entender B).Fabricar C).Espejo D).Clon",
    "10.Que significa la palabra *DIFF*\nA).Diferencia B).Otros C).Iguales D).Diccionario",
    "11.Que significa la palabra *CONFIG*\nA).Fabricacion B).Configuracion C).Destrucion D).Imaginacion",
    "12.Que significa la palabra *RESET*\nA).Suspendido B).Apagar C).Prender D).Reiniciar",
    "13.Que significa la palabra *STASH*\nA).Reserva B).Acumular C).Decender D).Status",
    "14.Que significa la palabra *SHORTLOG*\nA).Asta B).Emblema C).Bitacora D).Diccionario",
    "15.Que significa la palabra *HELP*\nA).Ayuda B).Servicios C).Ven D).Acercate",
    "16.Que significa la palabra *LIST*\nA).Lector B).Abreviado C).Lista D).Orden",
    "17.Que significa la palabra *CLEAN*\nA).Limpio B).Aceado C).Perfecto D).Configurar",
    "18.Que significa la palabra *VOID*\nA).Marco B).Borde C).Entero D).Vacio",
    "19.Que significa la palabra *BRANCH*\nA).Arbol B).Rama C).Sol D).Luz",
    "20.Que significa la palabra *BLAME*\nA).Culpar B).Enojo C).Rencor D).Culpa"
    }, Rpt[20]{
        "a", "a", "b", "d", "c", "d", "b", "a", "d", "a", "b", "d", "a", "c", "a", "c", "a", "d", "b", "a"
    };

int main(){
    for (int i = 1; i < 21; i++)
    {
     system("cls");
     cout<<preguntas[i-1]<<"\n\n"<<"--> ";
     cin>>valotario[i-1];

     if (valotario[i-1]==Rpt[i-1])
     {         
         calificacion[i-1]="Aprobado\t";
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
    archivo<<"========================================================================"<<endl;
    archivo<<"=                          Examen de Programacion                      ="<<endl;
    archivo<<"========================================================================\n"<<endl;
    for (int i = 1; i < 21; i++)
    {
     archivo<<preguntas[i-1]<<"\n";        
     archivo<<"\nLa respuesta "<<i<<" es:\t"<<valotario[i-1]<<" "<<calificacion[i-1]<<"||"<<" El correcto es: "<<Rpt[i-1]<<"\n\n";
    }
    archivo.close();
    system("Start examen.txt");    
}
