int led01=12,led02=11,led03=10,led04=9,led05=8, tiempo=100;
//Funcion modular
void parpadea(int LED){
  digitalWrite(LED, HIGH);
  delay(tiempo);
  digitalWrite(LED, LOW);
  delay(tiempo);
}

void setup() {
  pinMode(led01, OUTPUT);
  pinMode(led02, OUTPUT);
  pinMode(led03, OUTPUT);
  pinMode(led04, OUTPUT);
  pinMode(led05, OUTPUT);
}

void loop() {
  parpadea(led01);
  parpadea(led02);
  parpadea(led03);
  parpadea(led04);
  parpadea(led05);
}
