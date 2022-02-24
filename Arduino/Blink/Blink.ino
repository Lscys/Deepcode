
int led01=12, led02=11, led03=10, led04=9, led05=8, tiempo=100;
void setup()
{
  pinMode(led01, OUTPUT);
  pinMode(led02, OUTPUT);
  pinMode(led03, OUTPUT);
  pinMode(led04, OUTPUT);
  pinMode(led05, OUTPUT);
}

void loop()
{
  digitalWrite(led01, 1);//HIGH
  delay(tiempo);
  digitalWrite(led01, 0);//LOW
  delay(tiempo);

  digitalWrite(led02, HIGH);
  delay(tiempo);
  digitalWrite(led02, LOW);
  delay(tiempo);

  digitalWrite(led03, HIGH);
  delay(tiempo);
  digitalWrite(led03, LOW);
  delay(tiempo);

  digitalWrite(led04, HIGH);
  delay(tiempo);
  digitalWrite(led04, LOW);
  delay(tiempo);

  digitalWrite(led05, HIGH);
  delay(tiempo);
  digitalWrite(led05, LOW);
  delay(tiempo);
}

