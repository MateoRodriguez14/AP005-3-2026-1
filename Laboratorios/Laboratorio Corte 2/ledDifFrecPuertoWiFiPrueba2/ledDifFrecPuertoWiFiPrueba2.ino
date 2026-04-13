#include <WiFi.h>

const char* ssid = "MIREYA ";
const char* password = "52081344";
const int ledPin = 2;
char modo = '0';
unsigned long t0 = 0; //Almacena enteros no negativos de 0 a 4 mil millones
bool estadoLed = false;
int pasoDoble = 0;

WiFiServer server(3306);
WiFiClient client;


void setLed (bool estado){
  estadoLed = estado;
  digitalWrite(ledPin, estado ? HIGH : LOW); 
  //Operador ternario si estado == true selecciona HIGH      
}


void enviarRespuesta (const char* msg){
  Serial.println(msg);
  if(client && client.connected()){
    client.println(msg);
  }
}


void procesarComando (char c){
  switch(c){
    case '0':
      modo = '0';
      setLed(false);
      Serial.println("Modo 0: LED apagado");
      break;

    case '1':
      modo = '1';
      setLed(true);
      Serial.println("Modo 1: LED encendido fijo");
      break;

    case '2':
      modo = '2';
      t0 = millis();
      Serial.println("Modo 2: parpadeo lento");
      break;
    
    case '3':
     modo = '3';
     t0 = millis();
     Serial.println("Modo 3: parpadeo rapido");
     break;
  
    case '4':
      modo = '4';
      t0 = millis();
      pasoDoble = 0;
      setLed(false);
      Serial.println("Modo 4: doble destello");
      break;

    default: 
      Serial.print("Comando no valido: ");
      Serial.println(c);
      Serial.println("Usar 0, 1, 2, 3 o 4");
      break;
  }
}


void actualizarPatron(){
  unsigned long ahora = millis();
  switch(modo){
    case '0':
      break;

    case '1':
      break;

    case '2':
      if (ahora - t0 >= 500){
        t0 = ahora;
        setLed(!estadoLed);
      }
      break;
    
    case '3':
      if (ahora - t0 >= 150){
        t0 = ahora;
        setLed(!estadoLed);
      }
      break;
  
    case '4':
      switch(pasoDoble){
        case 0:
          setLed(true);
          pasoDoble = 1;
          t0 = ahora;
          break;
      
        case 1:
          if (ahora - t0 >= 100){
            setLed(false);
            pasoDoble = 2;
            t0 = ahora;
          }
          break;

        case 2:
          if (ahora - t0 >= 100){
            setLed(true);
            pasoDoble = 3;
            t0 = ahora;
          }
          break;

        case 3:
          if (ahora - t0 >= 100){
            setLed(false);
            pasoDoble = 4;
            t0 = ahora;
          }
          break;
        
        case 4:
          if (ahora - t0 >= 700){
            pasoDoble = 0;
            t0 = ahora;
          }
          break;
      }
      break;
  }
}

void conectarWiFi(){
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED){
    Serial.println(WiFi.status());
    delay(500);
    Serial.println(".");
  }
  Serial.println();
  Serial.println("WiFi conectada");
  Serial.println("IP del ESP32");
  Serial.println(WiFi.localIP());
}

void setup() {
  pinMode(ledPin, OUTPUT);
  setLed(false);
  Serial.begin(115200);
  delay(500);
  conectarWiFi();
  server.begin();
  Serial.println("Servidor TCP iniciando en puerto 3333");
  Serial.println("Comandos 0, 1, 2, 3, 4");

}

void loop() {
   if (!client || !client.connected()){
    WiFiClient nuevoCliente = server.available();
    if(nuevoCliente){
      client = nuevoCliente;
      Serial.println("Cliente Conectado");
      client.println("Conectado al ESP32");
      client.println("Comandos 0, 1, 2, 3, 4");
    }
  }
  if(client && client.connected()){
    while (client.available() > 0){
      char c = client.read();

      if(c!='\n' && c != '\r'){
        Serial.print("Recibido por WiFi: ");
        Serial.println(c);
        procesarComando(c);
      }
    }
  }
  actualizarPatron();
}
