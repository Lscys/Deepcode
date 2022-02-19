#include<iostream>
#include<conio.h>
using namespace std;
int V1, V2, Res;
int main(){
    for(V1=1; V1<=12; V1++){
        Res=V1*V2;
        cout<<V1<<"*"<<V2<<"="<<Res<<endl;
    }
    getch();
    return 0;
}