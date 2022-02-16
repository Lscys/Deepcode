#include<iostream>
#include<conio.h>//getch();
#include<stdio.h>//printf(""); C puro
#include<cstdlib>//system("CLS")
using namespace std;
int main(){
    int a=1, b=2, c=3;
    float numero=8;
    system("CLS");//limpiar pantalla
    printf("Hola mundo \n");
    cout<<"Hola mi gente \n";
    
    a+=5;
    printf("a+5=%d \n",a);
    c-=1;
    printf("c-1=%d \n",c);
    printf("%1.f \n",numero);

    b*=3;
    printf("b*3 = %d",b);
    getch();//pause
    return 0;
}