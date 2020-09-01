#include <SoftwareWire.h>
SoftwareWire myWire(2,3);
  const int outwo = 15; //White Orange Out - cat 5 pin 1
  const int outo = 14; //orange out - cat 5 pin 2
  const int outwg = 16; // White Green Out - cat 5 pin 3
  const int outg = 10; // Green out - cat 5 pin 6
  const int outwb = 18; // White Blue Out - cat 5 pin 5
  const int outb = 19; // Blue Out - cat 5 pin 4
  const int inb = 9; // Blue in - cat 5 pin 4
  const int inwb = 8; // White Blue In - cat 5 pin 5
  const int inwo = 4; // White Orange In - cat 5 pin 1
  const int ino = 5; // Orange in - cat 5 pin 2
  const int inwg = 6; // White Green In - cat 5 pin 3
  const int ing = 7; // Green in = cat 5 pin 6
  const int oe = 20; // OEL output for control
  const int sel = 21; // SEL output for control
  int cat1=0;
  int cat2=0;
  int cat3=0;
  int cat4=0;
  int cat5=0;
  int cat6=0;
void setup()
{
  myWire.begin(); // Wire communication begin
  Serial.begin(9600); // The baudrate of Serial monitor is set in 9600

  
  pinMode(outwo,OUTPUT);
  pinMode(outo,OUTPUT);
  pinMode(outwg,OUTPUT);
  pinMode(outg,OUTPUT);
  pinMode(outwb,OUTPUT);
  pinMode(outb,OUTPUT);
  pinMode(oe,OUTPUT);
  pinMode(sel,OUTPUT);
  pinMode(inwb,INPUT_PULLUP);
  pinMode(inb,INPUT_PULLUP);
  pinMode(inwo,INPUT_PULLUP);
  pinMode(ino,INPUT_PULLUP);
  pinMode(inwg,INPUT_PULLUP);
  pinMode(ing,INPUT_PULLUP);
  digitalWrite(outwo,HIGH);
  digitalWrite(outo,HIGH);
  digitalWrite(outwg,HIGH);
  digitalWrite(outg,HIGH);
  digitalWrite(outwb,HIGH); 
  digitalWrite(outb,HIGH);
  digitalWrite(oe,HIGH);
  digitalWrite(sel,HIGH);
}

void loop()
{
  digitalWrite(oe,LOW);
  digitalWrite(sel,LOW);
  digitalWrite(outwo,LOW);
  digitalWrite(outo,LOW);
  digitalWrite(outwg,LOW);
  digitalWrite(outg,LOW);
  digitalWrite(outwb,LOW); 
  digitalWrite(outb,LOW);
  cat1=digitalRead(inwo);
  cat2=digitalRead(ino);
  cat3=digitalRead(inwg);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  cat6=digitalRead(ing);
  Serial.println("OE1 and SEL LOW");
Serial.print("pin 1 ");
Serial.println(cat1);
Serial.print("pin 2 ");
Serial.println(cat2);
Serial.print("pin 3 ");
Serial.println(cat3);
Serial.print("pin 4 ");
Serial.println(cat4);
Serial.print("pin 5 ");
Serial.println(cat5);
Serial.print("pin 6 ");
Serial.println(cat6);
  Serial.println("OE1 LOW and SEL HIGH");
  digitalWrite(oe,LOW);
  digitalWrite(sel,HIGH);
  cat1=digitalRead(inwo);
  cat2=digitalRead(ino);
  cat3=digitalRead(inwg);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  cat6=digitalRead(ing);
Serial.print("pin 1 ");
Serial.println(cat1);
Serial.print("pin 2 ");
Serial.println(cat2);
Serial.print("pin 3 ");
Serial.println(cat3);
Serial.print("pin 4 ");
Serial.println(cat4);
Serial.print("pin 5 ");
Serial.println(cat5);
Serial.print("pin 6 ");
Serial.println(cat6);
  Serial.println("OE1 HIGH and SEL LOW");
  digitalWrite(oe,HIGH);
  digitalWrite(sel,LOW);
  cat1=digitalRead(inwo);
  cat2=digitalRead(ino);
  cat3=digitalRead(inwg);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  cat6=digitalRead(ing);
Serial.print("pin 1 ");
Serial.println(cat1);
Serial.print("pin 2 ");
Serial.println(cat2);
Serial.print("pin 3 ");
Serial.println(cat3);
Serial.print("pin 4 ");
Serial.println(cat4);
Serial.print("pin 5 ");
Serial.println(cat5);
Serial.print("pin 6 ");
Serial.println(cat6);
  Serial.println("OE1 and SEL HIGH");
  digitalWrite(oe,HIGH);
  digitalWrite(sel,HIGH);
  cat1=digitalRead(inwo);
  cat2=digitalRead(ino);
  cat3=digitalRead(inwg);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  cat6=digitalRead(ing);
Serial.print("pin 1 ");
Serial.println(cat1);
Serial.print("pin 2 ");
Serial.println(cat2);
Serial.print("pin 3 ");
Serial.println(cat3);
Serial.print("pin 4 ");
Serial.println(cat4);
Serial.print("pin 5 ");
Serial.println(cat5);
Serial.print("pin 6 ");
Serial.println(cat6);
    digitalWrite(oe,LOW);
  digitalWrite(sel,LOW);
  digitalWrite(outwo,HIGH);
  digitalWrite(outo,HIGH);
  digitalWrite(outwg,HIGH);
  digitalWrite(outg,HIGH);
  digitalWrite(outwb,HIGH); 
  digitalWrite(outb,HIGH);
    byte error, address; //variable for error and I2C address
  int nDevices;

  Serial.println("Scanning...");

  nDevices = 0;
  for (address = 1; address < 127; address++ )
  {
    // The i2c_scanner uses the return value of
    // the Write.endTransmisstion to see if
    // a device did acknowledge to the address.
    myWire.beginTransmission(address);
    error = myWire.endTransmission();

    if (error == 0)
    {
      Serial.print("I2C device found at address 0x");
      if (address < 16)
        Serial.print("0");
      Serial.print(address, HEX);
      Serial.println("  !");
      nDevices++;
    }
    else if (error == 4)
    {
      Serial.print("Unknown error at address 0x");
      if (address < 16)
        Serial.print("0");
      Serial.println(address, HEX);
    }
  }
  if (nDevices == 0)
    Serial.println("No I2C devices found\n");
  else
    Serial.println("done\n");
  
  
  delay(5000); // wait 5 seconds for the next I2C scan
}
