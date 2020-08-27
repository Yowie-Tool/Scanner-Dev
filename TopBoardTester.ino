#include <Wire.h> //include Wire.h library

void setup()
{
  Wire.begin(); // Wire communication begin
  Serial.begin(9600); // The baudrate of Serial monitor is set in 9600
  const int outwo = 13; //White Orange Out - cat 5 pin 1
  const int outo = 12; //orange out - cat 5 pin 2
  const int outwg = 11; // White Green Out - cat 5 pin 3
  const int outg = 10; // Green out - cat 5 pin 6
  const int outwb = 9; // White Blue Out - cat 5 pin 5
  const int outb = 8; // Blue Out - cat 5 pin 4
  const int inb = 7; // Blue in - cat 5 pin 4
  const int inwb = 6; // White Blue In - cat 5 pin 5
  const int inwo = 5; // White Orange In - cat 5 pin 1
  const int ino = 4; // Orange in - cat 5 pin 2
  const int inwg = 3; // White Green In - cat 5 pin 3
  const int ing = 2; // Green in = cat 5 pin 6
  const int oe = A0; // OEL output for control
  const int sel = A1; // SEL output for control
  int cat1=0;
  int cat2=0;
  int cat3=0;
  int cat4=0;
  int cat5=0;
  int cat6=0;
  
  pinMode(outwo,OUTPUT);
  pinMode(outo,OUTPUT);
  pinMode(outwg,OUTPUT);
  pinMode(outg,OUTPUT);
  pinMode(outwb,OUTPUT);
  pinMode(outb,OUTPUT);
  pinMode(oe,OUTPUT);
  pinMode(sel,OUTPUT);
  pinMode(inwb,INPUT);
  pinMode(inb,INPUT);
  pinMode(inwo,INPUT);
  pinMode(ino,INPUT);
  pinMode(inwg,INPUT);
  pinMode(ing,INPUT);
  digitalWrite(outwo,LOW);
  digitalWrite(outo,LOW);
  digitalWrite(outwg,LOW);
  digitalWrite(outg,LOW);
  digitalWrite(outwb,LOW); 
  digitalWrite(outb,LOW);
  digitalWrite(oe,LOW);
  digitalWrite(sel,LOW);
}

void loop()
{
  digitalWrite(oe,LOW);
  digitalWrite(sel,LOW);
  digitalWrite(outwo,HIGH);
  digitalWrite(outo,HIGH);
  digitalWrite(outwg,HIGH);
  digitalWrite(outg,HIGH);
  digitalWrite(outwb,HIGH); 
  digitalWrite(outb,HIGH);
  cat1=digitalRead(inwo);
  cat2=digitalRead(ino);
  cat3=digitalRead(inwg);
  cat4=digitalRead(inb);
  cat5=digitalRead(ino);
  cat6=digitalRead(ing);
  if (cat1==HIGH) Serial.println("pin 1 High");
  else Serial.println("pin 1 low");
  
  
  delay(5000); // wait 5 seconds for the next I2C scan
}
