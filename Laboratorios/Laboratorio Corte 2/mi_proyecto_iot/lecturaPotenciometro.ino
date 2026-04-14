// ============================================================
// PROYECTO: Lectura de un potenciometro con ESP32
// DESCRIPCION:
// 1. Lee un potenciometro conectado al ADC.
// 2. Convierte la lectura a voltaje aproximado.
// 3. Convierte la lectura a porcentaje.
// 4. Envia una linea CSV por puerto serial.
// AUTOR: Material pedagogico para Programacion Aplicada
// ============================================================
// ------------------------------------------------------------
// Pin analogico donde se conecta el terminal central del
// potenciometro. En ESP32, GPIO 34 es un pin de entrada.
// ------------------------------------------------------------
const int PIN_POT = 34;
// ------------------------------------------------------------
// Intervalo de muestreo en milisegundos.
// 500 ms significa 2 muestras por segundo.
// ------------------------------------------------------------
const unsigned long INTERVALO_MS = 500;
// ------------------------------------------------------------
// Variable que almacena el instante de la ultima transmision.
// Se compara con millis() para no bloquear el programa.
// ------------------------------------------------------------
unsigned long ultimoEnvio = 0;
// ------------------------------------------------------------
// setup():
// Se ejecuta una sola vez al encender o reiniciar la placa.
// ------------------------------------------------------------
void setup() {
  // Inicializa la comunicacion serial a 115200 baudios.
  Serial.begin(115200);
  // Pausa corta para estabilizar la conexion con el PC.
  delay(1000);
  // Configura la resolucion del ADC a 12 bits.
  // Eso produce valores entre 0 y 4095.
  analogReadResolution(12);
  // Se deja explicito que el pin se usara como entrada.
  pinMode(PIN_POT, INPUT);
  // Mensaje informativo de arranque.
  Serial.println("ESP32 listo. Enviando: lectura_cruda,voltaje,porcentaje");
}
// ------------------------------------------------------------
// loop():
// Se ejecuta repetidamente mientras la placa esta encendida.
// ------------------------------------------------------------
void loop() {
  // Tiempo actual desde el arranque de la placa.
  unsigned long ahora = millis();
  // Solo se envia una muestra cuando se cumple el intervalo.
  if (ahora - ultimoEnvio >= INTERVALO_MS) {
  // Se actualiza el instante de referencia.
  ultimoEnvio = ahora;
  // Lectura cruda del ADC.
  int lecturaCruda = analogRead(PIN_POT);
  // Conversion aproximada a voltaje suponiendo 3.3 V maximos.
  float voltaje = (lecturaCruda / 4095.0) * 3.3;
  // Conversion aproximada a porcentaje de 0 a 100.
  int porcentaje = map(lecturaCruda, 0, 4095, 0, 100);
  // Envio en formato CSV:
  // lectura_cruda,voltaje,porcentaje
  Serial.print(lecturaCruda);
  Serial.print(",");
  Serial.print(voltaje, 3);
  Serial.print(",");
  Serial.println(porcentaje);
  }
}

