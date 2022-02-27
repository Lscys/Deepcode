//Variables Globales
int led01=12, led02=11,led03=10, led04=9, led05=8;
boolean ledOn01=false, ledOn02=false, ledOn03=false, ledOn04=false, ledOn05=false;

//Funcion Global

void toggle01(int Led){//Led es un aragumento local huesped
  ledOn01=!ledOn01;
  digitalWrite(Led, ledOn01);
  
}

void toggle02(int led){
  ledOn02=!ledOn02;
  digitalWrite(led, ledOn02);
}

void toggle03(int led){
  ledOn03=!ledOn03;
  digitalWrite(led, ledOn03);
}

void toggle04(int led){
  ledOn04=!ledOn04;
  digitalWrite(led, ledOn04);
}

void toggle05(int led){
  ledOn05=!ledOn05;
  digitalWrite(led, ledOn05);
}

void setup() {
  Serial.begin(9600);
  pinMode(led01, OUTPUT);
  pinMode(led02, OUTPUT);
  pinMode(led03, OUTPUT);
  pinMode(led04, OUTPUT);
  pinMode(led05, OUTPUT);
}

void loop() {
  //Variables Locales
  //Funcion Local
  //Estados:
//HIGH = estado Alto = 1 = true
//LOW = Estado bajo = 0 = false
char teclado = Serial.read();
if(teclado=='a'){toggle01(led01);}//argumento ejecutor
if(teclado=='s'){toggle02(led02);}
if(teclado=='d'){toggle03(led03);}
if(teclado=='f'){toggle04(led04);}
if(teclado=='g'){toggle05(led05);}
}
