
#  Lectura de Potenciometro con ESP 32

## Descripción

Actividad didactica cuyo objetivo práctico reside en tomar lecturas continuas de los valores generados por un potenciometro (voltaje, porcentaje reistencia potenciómetro) mediante el ESP 32 para posteriormente evaluar estos datos y mostrarlos con Python y HTML respectivamente.

## Características

-  Recepción de datos analogicos de forma serial
-  Visualización en tiempo real
-  Interfaz gráfica sencilla

## Tecnologías

- Python 3
- Flask
- ESP32 (Arduino IDE)
- HTML y CSS

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/MateoRodriguez14/AP005-3-2026-1.git
````

2. Entrar al directorio:

```bash
cd Laboratorios\Laboratorio Corte 2\mi_proyecto_iot
```

## Instrucciones de uso.
- Cargar el programa lecturaPotenciometro.ino en el ESP32
- Ejecute el archivo serial_a_csv.py
- Ejecute el archivo app.py
- En su navegador de preferencia dirijase al enlace: http://127.0.0.1:5000/
##  Estructura del proyecto

```
mi_proyecto_iot/
|-- lecturaPotenciometro.ino
|-- app.py
|-- serial_a_csv.py
|-- datos_potenciometro.csv
|-- requirements.txt
|
|-- templates/
| ‘-- index.html
|
‘-- static/
‘-- grafica_potenciometro.png
```

## Resultados
<img width="1920" height="974" alt="Captura de pantalla (743)" src="https://github.com/user-attachments/assets/3ab42be1-3dfc-4c25-87fc-d182fdec7d91" />

<img width="1920" height="917" alt="Captura de pantalla (744)" src="https://github.com/user-attachments/assets/d3b36c80-5cc3-44eb-8017-ea3f9e9e46e6" />

