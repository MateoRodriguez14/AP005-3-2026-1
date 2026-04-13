const int ledPin = 2;


void setup() {
  Serial.begin(115200);
  Serial.println("Inicio de aplicacion");
  Serial.println("Esperando Tecla...");
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
      char tecla = Serial.read();  // Lee 1 carácter
      if (tecla == 'w' || tecla == 's'){
        digitalWrite(ledPin, HIGH);
      }
      else{
        digitalWrite(ledPin, LOW);
      }
  }
}