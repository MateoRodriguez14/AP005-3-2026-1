from machine import Pin
import time
pinEntrada = Pin(23, Pin.IN)
listaPuertos = [15, 2, 4, 16, 17, 5, 18, 19]
while True:
    for i in listaPuertos:
        pinSalida = Pin(i, Pin.OUT)
        pinSalida.on()
        time.sleep(1)
        pinSalida.off()