import socket
import keyboard

ipEsp32 = "192.168.0.6"
puerto = 3306




def main(datosTeclado):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ipEsp32, puerto))
    except TimeoutError as e:
        print("Tiempo de espera conexion elevado")   
        print(e)

    print("Conectado al ESP32")

    try:
        sock.settimeout(1)
        try:
            data = sock.recv(1024)
            if data:
                print(data.decode(errors="ignore"))
        except:
            pass

        #while True:
            #cmd = keyboard.read_event()
            #if len(cmd) > 0:
            #sock.send(cmd[0].encode())
        sock.send(datosTeclado.encode())
        print(f"Se ha enviado correctamente  {datosTeclado}  al ESP32")
            #print("Enviado: ",cmd.name.encode())

        try:
            respuesta = sock.recv(1024)
            if respuesta:
                print("ESP32: ", respuesta.decode(errors="ignore").strip())
        except:
            pass
    except Exception as error:
        print("Ha ocurrido un error: ", error)
    '''
    finally:
        sock.close()
        print("Conexión cerrada")
        '''