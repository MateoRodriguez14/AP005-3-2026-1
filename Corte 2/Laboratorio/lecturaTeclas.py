import serial
import keyboard
import serial.tools.list_ports
import time


puerto = "COM3"
baudRate = 115200

print("Puertos disponibles: ")
for p in serial.tools.list_ports.comports():
    print (".", p.device, "-", p.description)

ser = None

try:
    ser = serial.Serial(puerto, baudRate, timeout=1)
    time.sleep(2)
    print(f"Conectado en {puerto}")
    while True:
        tecla = keyboard.read_event()
        #if tecla.event_type==keyboard.KEY_UP:
        ser.write(tecla.name.encode())

except serial.SerialException as e:
    print("No se pudo abrir el puerto.")
    print("Detalle del error: ")
    print(e)
finally:
    if ser is not None and ser.is_open:
        ser.close()
        print("Puerto cerrado")