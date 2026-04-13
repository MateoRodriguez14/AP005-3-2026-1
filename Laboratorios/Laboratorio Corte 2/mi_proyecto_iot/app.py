"""
============================================================
PROYECTO: Servidor web con Flask para visualizar datos del CSV
DESCRIPCION:
1. Lee el archivo CSV generado por serial_a_csv.py.
2. Usa pandas para convertir el CSV en una tabla.
3. Usa matplotlib para generar una grafica PNG.
4. Usa Flask para servir una pagina HTML con resumen, tabla y grafica.
AUTOR: Material pedagogico para Programacion Aplicada
============================================================
"""
# ---------------------------------------------------------
# Importacion de modulos
# ---------------------------------------------------------
import os
from datetime import datetime
# Flask crea la aplicacion web y render_template carga el HTML.
from flask import Flask, render_template
# pandas lee el CSV y permite trabajar con tablas.
import pandas as pd
from pandas.errors import EmptyDataError
# matplotlib se configura con el backend Agg para generar
# imagenes sin abrir ventanas graficas.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# ---------------------------------------------------------
# Configuracion principal
# ---------------------------------------------------------
ARCHIVO_CSV = "Laboratorios/Laboratorio Corte 2/mi_proyecto_iot/datos_potenciometro.csv"
CARPETA_STATIC = "Laboratorios/Laboratorio Corte 2/mi_proyecto_iot/static"
RUTA_GRAFICA = os.path.join(CARPETA_STATIC, "grafica_potenciometro.png")
# Se crea la aplicacion Flask.
app = Flask(__name__)
# ---------------------------------------------------------
# Cargar datos del CSV
# ---------------------------------------------------------
def cargar_datos():
    # Si el archivo aun no existe, se devuelve una tabla vacia.
    if not os.path.exists(ARCHIVO_CSV):
        return pd.DataFrame()
    try:
        # Se lee el CSV y se interpreta timestamp_pc como fecha.
        df = pd.read_csv(ARCHIVO_CSV, parse_dates=["timestamp_pc"])
        # Si el archivo existe pero esta vacio, se devuelve una tabla vacia.
        if df.empty:
            return pd.DataFrame()
        # Conversion segura de columnas numericas.
        df["lectura_cruda"] = pd.to_numeric(df["lectura_cruda"], errors="coerce")
        df["voltaje"] = pd.to_numeric(df["voltaje"], errors="coerce")
        df["porcentaje"] = pd.to_numeric(df["porcentaje"], errors="coerce")
        # Eliminacion de filas con datos no convertibles.
        df = df.dropna().reset_index(drop=True)
        return df
    except EmptyDataError:
        # Ocurre si el archivo existe pero no tiene contenido util.
        return pd.DataFrame()
    except KeyError as error:
        # Ocurre si falta alguna columna esperada.
        print(f"[ERROR] Falta una columna en el CSV: {error}")
        return pd.DataFrame()
    except Exception as error:
        # Cualquier otro error se informa y se retorna tabla vacia.
        print(f"[ERROR] No se pudo cargar el CSV: {error}")
        return pd.DataFrame()
# ---------------------------------------------------------
# Generar la grafica PNG
# ---------------------------------------------------------
def generar_grafica(df):
    # Se crea la carpeta static si aun no existe.
    os.makedirs(CARPETA_STATIC, exist_ok=True)
    try:
        # Si no hay datos, se crea una imagen informativa.
        if df.empty:
            plt.figure(figsize=(10, 4))
            plt.text(0.5, 0.5, "Aun no hay datos para graficar",
            ha="center", va="center", fontsize=14)
            plt.axis("off")
            plt.tight_layout()
            plt.savefig(RUTA_GRAFICA)
            plt.close()
            return
        # Se toman solo las ultimas 100 muestras.
        df_grafica = df.tail(100).copy()
        # Se crea la figura y se grafica la lectura cruda.
        plt.figure(figsize=(12, 5))
        plt.plot(df_grafica["timestamp_pc"], df_grafica["lectura_cruda"], marker="o")
        plt.title("Lecturas recientes del potenciometro")
        plt.xlabel("Tiempo")
        plt.ylabel("Lectura ADC (0 a 4095)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(RUTA_GRAFICA)
        plt.close()
    except Exception as error:
        print(f"[ERROR] No se pudo generar la grafica: {error}")
# ---------------------------------------------------------
# Construir resumen numerico
# ---------------------------------------------------------
def construir_resumen(df):
    # Si no hay datos, se devuelve un resumen por defecto.
    if df.empty:
        return {
            "total_muestras": 0,
            "ultima_lectura": "Sin datos",
            "ultimo_voltaje": "Sin datos",
            "ultimo_porcentaje": "Sin datos",
            "promedio": "Sin datos",
            "minimo": "Sin datos",
            "maximo": "Sin datos",
        }
    # Ultima fila del DataFrame.
    ultima = df.iloc[-1]
    # Diccionario con estadisticas basicas.
    return {
        "total_muestras": int(len(df)),
        "ultima_lectura": int(ultima["lectura_cruda"]),
        "ultimo_voltaje": round(float(ultima["voltaje"]), 3),
        "ultimo_porcentaje": round(float(ultima["porcentaje"]), 1),
        "promedio": round(float(df["lectura_cruda"].mean()), 2),
        "minimo": int(df["lectura_cruda"].min()),
        "maximo": int(df["lectura_cruda"].max()),
    }
# ---------------------------------------------------------
# Ruta principal
# ---------------------------------------------------------
@app.route("/")
def inicio():
    try:
        # 1. Cargar los datos del CSV.
        df = cargar_datos()
        # 2. Generar la imagen de la grafica.
        generar_grafica(df)
        # 3. Construir el resumen estadistico.
        resumen = construir_resumen(df)
        # 4. Construir una tabla HTML con las ultimas 10 filas.
        if df.empty:
            tabla_html = "<p>No hay datos todavia.</p>"
        else:
            tabla_html = (
                df.tail(10)
                .copy()
                .to_html(classes="tabla-datos", index=False, border=0)
            )
        # 5. Hora de actualizacion.
        actualizacion = datetime.now().strftime(" %Y- %m- %d %H: %M: %S")
        # 6. Renderizado del template HTML.
        return render_template(
            "index.html",
            resumen=resumen,
            tabla_html=tabla_html,
            actualizacion=actualizacion
        )
    except Exception as error:
        # Si algo falla dentro de la ruta, se devuelve una pagina
        # simple de error para no dejar al usuario sin respuesta.
        return f"""
        <html>
        <head><title>Error del servidor</title></head>
        <body>
        <h1>Error interno en la aplicacion</h1>
        <p>Detalle: {error}</p>
        </body>
        </html>
        """, 500
# ---------------------------------------------------------
# Ejecucion del servidor Flask
# ---------------------------------------------------------
if __name__ == "__main__":
    # debug=True es util durante el desarrollo.
    # En un entorno real de produccion no se recomienda.
    app.run(host="0.0.0.0", port=5000, debug=True)

