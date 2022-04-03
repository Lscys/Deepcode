#include<iostream>
#include<conio.h>
#include<string.h>
#include<fstream>

using namespace std;

string respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, respuesta6, respuesta7, respuesta8, respuesta9, respuesta10, respuesta11, respuesta12, respuesta13, respuesta14, respuesta15, respuesta16, respuesta17, respuesta18, respuesta19, respuesta20;
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

    cout<<"4.Que significa la palabra *PULL*"<<endl;
    cout<<"A).Ver B).Dar C).Atender D).Jalar\n";
    cin>>respuesta4;

    cout<<"5.Que significa la palabra *STAT*"<<endl;
    cout<<"A).Numeros B).Letras C).Estadistica D).Multiplicacion\n";
    cin>>respuesta5;

    cout<<"6.Que significa la palabra *ADD*"<<endl;
    cout<<"A).Adentrar B).Despojar C).Pedir D).Agregar\n";
    cin>>respuesta6;

    cout<<"7.Que significa la palabra *ALL*"<<endl;
    cout<<"A).Ustedes B).Todos C).Ellos D).Aquellos\n";
    cin>>respuesta7;

    cout<<"8.Que significa la palabra *MAIN*"<<endl;
    cout<<"A).Principal B).Secundario C).Octavo D).Decimo\n";
    cin>>respuesta8;

    cout<<"9.Que significa la palabra *CLONE*"<<endl;
    cout<<"A).Entender B).Fabricar C).Espejo D).Clon\n";
    cin>>respuesta9;

    cout<<"10.Que significa la palabra *DIFF*"<<endl;
    cout<<"A).Diferencia B).Otros C).Iguales D).Diccionario\n";
    cin>>respuesta10;

    cout<<"11.Que significa la palabra *CONFIG*"<<endl;
    cout<<"A).Fabricacion B).Configuracion C).Destrucion D).Imaginacion\n";
    cin>>respuesta11;

    cout<<"12.Que significa la palabra *RESET*"<<endl;
    cout<<"A).Suspendido B).Apagar C).Prender D).Reiniciar\n";
    cin>>respuesta12;

    cout<<"13.Que significa la palabra *STASH*"<<endl;
    cout<<"A).Reserva B).Acumular C).Decender D).Status\n";
    cin>>respuesta13;

    cout<<"14.Que significa la palabra *SHORTLOG*"<<endl;
    cout<<"A).Asta B).Emblema C).Bitacora D).Diccionario\n";
    cin>>respuesta14;

    cout<<"15.Que significa la palabra *HELP*"<<endl;
    cout<<"A).Ayuda B).Servicios C).Ven D).Acercate\n";
    cin>>respuesta15;
    
    cout<<"16.Que significa la palabra *LIST*"<<endl;
    cout<<"A).Lector B).Abreviado C).Lista D).Orden\n";
    cin>>respuesta16;

    cout<<"17.Que significa la palabra *CLEAN*"<<endl;
    cout<<"A).Limpio B).Aceado C).Perfecto D).Configurar\n";
    cin>>respuesta17;

    cout<<"18.Que significa la palabra *VOID*"<<endl;
    cout<<"A).Marco B).Borde C).Entero D).Vacio\n";
    cin>>respuesta18;
    
    cout<<"19.Que significa la palabra *BRANCH*"<<endl;
    cout<<"A).Arbol B).Rama C).Sol D).Luz\n";
    cin>>respuesta19;

    cout<<"20.Que significa la palabra *BLAME*"<<endl;
    cout<<"A).Culpar B).Enojo C).Rencor D).Culpa\n";
    cin>>respuesta20;
     
    
    if (respuesta1 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta2 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta3 == "B") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta4 == "D") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta5 == "C") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta6 == "D") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta7 == "B") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta8 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta9 == "D") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta10 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta11 == "B") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta12 == "D") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta13 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta14 == "C") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta15 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta16 == "C") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta17 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta18 == "D") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta19 == "B") {
        rpt++;
    }else{
        rptn++;
    }
    if (respuesta20 == "A") {
        rpt++;
    }else{
        rptn++;
    }
    getch();
    ofstream archivo;
    archivo.open("test.txt");
    cout<<"Las corectas son: "<<rpt<<"\n";
    cout<<"Las incorrectas son: "<<rptn<<"\n";

    if (respuesta1 == "A") {
        archivo<<"Respuesta 1. Correcta\n";
    }else{
        archivo<<"Respuesta 1. Incorrecta\n";
    }
    if (respuesta2 == "A") {
        archivo<<"Respuesta 2. Correcta\n";
    }else{
        archivo<<"Respuesta 2. Incorrecta\n";
    }
    if (respuesta3 == "B") {
        archivo<<"Respuesta 3. Correcta\n";
    }else{
        archivo<<"Respuesta 3. Incorrecta\n";
    }
    if (respuesta4 == "D") {
        archivo<<"Respuesta 4. Correcta\n";
    }else{
        archivo<<"Respuesta 4. Incorrecta\n";
    }
    if (respuesta5 == "C") {
        archivo<<"Respuesta 5. Correcta\n";
    }else{
        archivo<<"Respuesta 5. Incorrecta\n";
    }
    if (respuesta6 == "D") {
        archivo<<"Respuesta 6. Correcta\n";
    }else{
        archivo<<"Respuesta 6. Incorrecta\n";
    }
    if (respuesta7 == "B") {
        archivo<<"Respuesta 7. Correcta\n";
    }else{
        archivo<<"Respuesta 7. Incorrecta\n";
    }
    if (respuesta8 == "A") {
        archivo<<"Respuesta 8. Correcta\n";
    }else{
        archivo<<"Respuesta 8. Incorrecta\n";
    }
    if (respuesta9 == "D") {
        archivo<<"Respuesta 9. Correcta\n";
    }else{
        archivo<<"Respuesta 9. Incorrecta\n";
    }
    if (respuesta10 == "A") {
        archivo<<"Respuesta 10. Correcta\n";
    }else{
        archivo<<"Respuesta 10. Incorrecta\n";
    }
    if (respuesta11 == "B") {
        archivo<<"Respuesta 11. Correcta\n";
    }else{
        archivo<<"Respuesta 11. Incorrecta\n";
    }
    if (respuesta12 == "D") {
        archivo<<"Respuesta 12. Correcta\n";
    }else{
        archivo<<"Respuesta 12. Incorrecta\n";
    }
    if (respuesta13 == "A") {
        archivo<<"Respuesta 13. Correcta\n";
    }else{
        archivo<<"Respuesta 13. Incorrecta\n";
    }
    if (respuesta14 == "C") {
        archivo<<"Respuesta 14. Correcta\n";
    }else{
        archivo<<"Respuesta 14. Incorrecta\n";
    }
    if (respuesta15 == "A") {
        archivo<<"Respuesta 15. Correcta\n";
    }else{
        archivo<<"Respuesta 15. Incorrecta\n";
    }
    if (respuesta16 == "C") {
        archivo<<"Respuesta 16. Correcta\n";
    }else{
        archivo<<"Respuesta 16. Incorrecta\n";
    }
    if (respuesta17 == "A") {
        archivo<<"Respuesta 17. Correcta\n";
    }else{
        archivo<<"Respuesta 17. Incorrecta\n";
    }
    if (respuesta18 == "D") {
        archivo<<"Respuesta 18. Correcta\n";
    }else{
        archivo<<"Respuesta 18. Incorrecta\n";
    }
    if (respuesta19 == "B") {
        archivo<<"Respuesta 19. Correcta\n";
    }else{
        archivo<<"Respuesta 19. Incorrecta\n";
    }
    if (respuesta20 == "A") {
        archivo<<"Respuesta 20. Correcta\n";
    }else{
        archivo<<"Respuesta 20. Incorrecta\n";
    }
    archivo.close();
    system("Start test.txt");

    return 0;
}