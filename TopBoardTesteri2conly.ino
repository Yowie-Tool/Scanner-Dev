  const int outb = 16; // White Green Out - cat 5 pin 3
  const int outwb = 10; // Green out - cat 5 pin 6
  const int inb = 8; // Blue in - cat 5 pin 4
  const int inwb = 9; // White Blue In - cat 5 pin 5
  const int oe = 11; // OEL output for control
  const int sel = 12; // SEL output for control
  const int swfault = 21; //orange out - cat 5 pin 2
  int cat4=0;
  int cat5=0;
  int swfaultstatus=0;
void setup()
{
  Serial.begin(9600); // The baudrate of Serial monitor is set in 9600

  pinMode(outwb,OUTPUT);
  pinMode(outb,OUTPUT);
  pinMode(swfault, INPUT_PULLUP);
  pinMode(inwb,INPUT_PULLUP);
  pinMode(inb,INPUT_PULLUP);
  pinMode(sel,OUTPUT);
  pinMode(oe,OUTPUT);
  digitalWrite(outwb,HIGH); 
  digitalWrite(outb,HIGH);
  digitalWrite(sel,LOW); 
  digitalWrite(oe,LOW);
  
}

void loop(){
  swfaultstatus=digitalRead(swfault);
  Serial.print("Switch Fault ");
  Serial.println(swfaultstatus);
  Serial.print("SEL and OE Low");
  digitalWrite(sel,LOW); 
  digitalWrite(oe,LOW);
  digitalWrite(outb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outb,HIGH);
Serial.print("Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  digitalWrite(outwb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outwb,HIGH);
Serial.print("White Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  swfaultstatus=digitalRead(swfault);
  Serial.print("Switch Fault ");
  Serial.println(swfaultstatus);
  Serial.print("SEL HIGH and OE Low");
  digitalWrite(sel,HIGH); 
  digitalWrite(oe,LOW);
  digitalWrite(outb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outb,HIGH);
Serial.print("Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  digitalWrite(outwb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outwb,HIGH);
Serial.print("White Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  swfaultstatus=digitalRead(swfault);
  Serial.print("Switch Fault ");
  Serial.println(swfaultstatus);
  Serial.print("SEL LOW and OE HIGH");
  digitalWrite(sel,LOW); 
  digitalWrite(oe,HIGH);
  digitalWrite(outb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outb,HIGH);
Serial.print("Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  digitalWrite(outwb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outwb,HIGH);
Serial.print("White Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  swfaultstatus=digitalRead(swfault);
  Serial.print("Switch Fault ");
  Serial.println(swfaultstatus);
  Serial.print("SEL and OE HIGH");
  digitalWrite(sel,HIGH); 
  digitalWrite(oe,HIGH);
  digitalWrite(outb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outb,HIGH);
Serial.print("Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  digitalWrite(outwb,LOW);
  cat4=digitalRead(inb);
  cat5=digitalRead(inwb);
  digitalWrite(outwb,HIGH);
Serial.print("White Brown Low Out ");
Serial.println(cat4);
Serial.println(cat5);

  
  delay(5000); // 
}
