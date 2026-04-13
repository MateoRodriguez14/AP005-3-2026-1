
#  ESP32 WiFi Monitor

Proyecto para monitorear datos enviados desde un ESP32 a través de WiFi y visualizarlos en Python.

## Descripción

Este proyecto permite capturar datos enviados por un ESP32 y mostrarlos en una interfaz gráfica desarrollada con Tkinter.

## Características

-  Recepción de datos por WiFi
-  Visualización en tiempo real
-  Interfaz gráfica sencilla
-  Compatible con ESP32

## Tecnologías

- Python 3
- Tkinter
- ESP32 (Arduino IDE)
- WiFi

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/esp32-wifi-monitor.git
````

2. Entrar al directorio:

```bash
cd esp32-wifi-monitor
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

##  Uso

Ejecuta el programa principal:

```bash
python main.py
```

Asegúrate de que el ESP32 esté conectado a la misma red WiFi.

##  Estructura del proyecto

```
esp32-wifi-monitor/
│── main.py
│── wifi_receiver.py
│── gui/
│   └── interfaz.py
│── requirements.txt
│── README.md
```

##  Configuración

Modifica la IP del servidor en el archivo `wifi_receiver.py`:

```python
HOST = "192.168.1.100"
PORT = 5000
```

##  Contribuciones

1. Haz un fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit (`git commit -m "Agrega nueva funcionalidad"`)
4. Haz push (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

##  Licencia

Este proyecto está bajo la licencia MIT.

##  Autor

Tu Nombre - [@tu-usuario](https://github.com/tu-usuario)

```
```
