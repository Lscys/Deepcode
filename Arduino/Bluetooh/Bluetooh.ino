#include"SoftwareSerial.h"
SoftwareSerial BT(2,3);//2 es RX, 3 es TX
int led01=13, led02=12, led03=11, led04=10, led05=9, led06=8, led07=7, led08=6, led09=5, led10=4;
boolean ledOn01=false, ledOn02=false, ledOn03=false, ledOn04=false, ledOn05=false, ledOn06=false, ledOn07=false, ledOn08=false, ledOn09=false, ledOn10=false;
void toggle01(int Led){//argumento
  ledOn01=!ledOn01;
  digitalWrite(Led, ledOn01);

}
void toggle02(int Led){//argumento
  ledOn02=!ledOn02;
  digitalWrite(Led, ledOn02);

}
void toggle03(int Led){//argumento
  ledOn03=!ledOn03;
  digitalWrite(Led, ledOn03);

}
void toggle04(int Led){//argumento
  ledOn04=!ledOn04;
  digitalWrite(Led, ledOn04);

}
void toggle05(int Led){//argumento
  ledOn05=!ledOn05;
  digitalWrite(Led, ledOn05);

}
void toggle06(int Led){//argumento
  ledOn06=!ledOn06;
  digitalWrite(Led, ledOn06);

}
void toggle07(int Led){//argumento
  ledOn07=!ledOn07;
  digitalWrite(Led, ledOn07);

}
void toggle08(int Led){//argumento
  ledOn08=!ledOn08;
  digitalWrite(Led, ledOn08);

}
void toggle09(int Led){//argumento
  ledOn09=!ledOn09;
  digitalWrite(Led, ledOn09);

}
void toggle10(int Led){//argumento
  ledOn10=!ledOn10;
  digitalWrite(Led, ledOn10);

}
void setup() {
  Serial.begin(9600); //comunicion por puerto serie USB
  BT.begin(9600);
  pinMode(led01, OUTPUT);
  pinMode(led02, OUTPUT);
  pinMode(led03, OUTPUT);
  pinMode(led04, OUTPUT);
  pinMode(led05, OUTPUT);
  pinMode(led06, OUTPUT);
  pinMode(led07, OUTPUT);
  pinMode(led08, OUTPUT);
  pinMode(led09, OUTPUT);
  pinMode(led10, OUTPUT);

}

void loop() {

  if (Serial.available() > 0) {//Trabaja con el serial fisico
    char teclado = Serial.read();

    if(teclado=='a'){toggle01(led01);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='s'){toggle02(led02);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='d'){toggle03(led03);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='f'){toggle04(led04);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='g'){toggle05(led05);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='h'){toggle06(led06);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='j'){toggle07(led07);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='k'){toggle08(led08);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='l'){toggle09(led09);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='q'){toggle10(led10);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
      
  }

  if (BT.available() > 0) {
    char teclado = BT.read();

    if(teclado=='a'){toggle01(led01);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='s'){toggle02(led02);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='d'){toggle03(led03);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='f'){toggle04(led04);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='g'){toggle05(led05);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='h'){toggle06(led06);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='j'){toggle07(led07);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='k'){toggle08(led08);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='l'){toggle09(led09);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
    if(teclado=='q'){toggle10(led10);
      Serial.write(teclado);
      Serial.println();
      delay(50);
    }
      
  }
  
  
  
}
