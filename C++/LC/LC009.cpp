#include<iostream>
#include<math.h>
using namespace std;
float Area, P, A, B, C;
int main(){
    cout<<"Ingrese lado 1: ";
    cin>>A;
    cout<<"Ingrese lado 2: ";
    cin>>B;
    cout<<"Ingrese lado 3: ";
    cin>>C;
    P=(A+B+C)/2;
    Area=(P*(P-A)*(P-B)*(P-C));
    cout<<"El area es: "<<Area;
    return 0;
}