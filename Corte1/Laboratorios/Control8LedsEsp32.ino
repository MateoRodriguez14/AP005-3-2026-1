int listaPines[8] = {15, 2, 4, 16, 17, 5, 18, 19};
const int pinEntradaPulsador = 23;
void setup() {
  Serial.begin(115200);
  pinMode(pinEntradaPulsador, INPUT);
  for(int i = 0; i < 8; i++) {
    Serial.println(listaPines[i]);
    pinMode(listaPines[i], OUTPUT);
  }

}

void loop() {
  for (int i = 0; i < 8; i++) {
    revisaryActivarDesactivarFuncionBoton(listaPines);
    digitalWrite(listaPines[i], HIGH);
    delay(500);
    digitalWrite(listaPines[i], LOW);
  }
  for (int i = 8; i > 0; i--) {
    revisaryActivarDesactivarFuncionBoton(listaPines);
    digitalWrite(listaPines[i], HIGH);
    delay(500);
    digitalWrite(listaPines[i], LOW);
  }
}

void revisaryActivarDesactivarFuncionBoton(int listaPinesSalida[8]){
  int EstadoBoton = digitalRead(pinEntradaPulsador);
  if(EstadoBoton == HIGH){
    for(int i = 0; i < 8 ; i +=2){
      digitalWrite(listaPinesSalida[i], HIGH);
    }
  }
  else{
    for(int i = 0; i < 8 ; i +=2){
      digitalWrite(listaPinesSalida[i], LOW);
    }
  }
}
