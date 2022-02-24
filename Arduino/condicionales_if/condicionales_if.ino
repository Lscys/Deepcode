int led01=12,led02=11;
void setup() {
  Serial.begin(9600);//Abro la lectura del puerto usb
  pinMode(led01, OUTPUT);
  pinMode(led02, OUTPUT);
}

void loop() {
  char teclado = Serial.read();
  if(teclado=='a'){digitalWrite(led01, HIGH);}
  if(teclado=='s'){digitalWrite(led01, LOW);}
  if(teclado=='d'){digitalWrite(led02, HIGH);}
  if(teclado=='f'){digitalWrite(led02, LOW);}
}
