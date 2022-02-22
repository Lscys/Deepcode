#include<iostream>
#include<stdlib.h>//system("cls"); Limpiar pantalla PAUSE
#include<ctime>
#include<conio.h>
using namespace std;
void cabezera(){
    cout<<"---------------------------- \n";
    cout<<"Instituto de Educacion Superior Computronic Tech \n";
    cout<<"Lideres en Computacion \n";
    cout<<"Av. Uruguay 360 - Lima \n";
    cout<<"Telefono: 424-5715/Fax 323-5750 \n";
    cout<<"----------------------------- \n";
    cout<<"----------------------------- \n";
}
void delay(int secs){
    for(int i=(time(NULL) + secs); time(NULL)!= i; time(NULL));
}

int main(){
    cabezera();
    cout<<"Computacion y Sistemas \n";
    delay(5);
    //getch();//pause
    system("cls");
    cabezera();
    cout<<"Cursos libres de computacion \n";
    return 0;
}