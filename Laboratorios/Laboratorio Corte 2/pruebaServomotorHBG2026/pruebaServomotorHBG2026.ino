int servoPin = 18;

void setup() {
  Serial.begin(115200);
  pinMode(servoPin, OUTPUT);
}

void loop() {

  int i = 0;

  while (i < 50) {
    digitalWrite(servoPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(servoPin, LOW);
    delayMicroseconds(12000);
    i++;
  }

  i = 0;

  while (i < 50) {
    digitalWrite(servoPin, HIGH);
    delayMicroseconds(2000);
    digitalWrite(servoPin, LOW);
    delayMicroseconds(12000);
    i++;
  }

}