import os
from flask import Flask, render_template, request, jsonify
import lecturaTecladoII 

app = Flask(__name__)
@app.route("/")
def inicio():
    try:
        return render_template("index.html")  
    except Exception as error:
        return f"""
        <html>
        <head><title>Error del servidor</title></head>
        <body>
        <h1>Error interno en la aplicacion</h1>
        <p>Detalle: {error}</p>
        </body>
        </html>
        """, 

@app.route("/lectura", methods=['POST'])
def lecturaDatos():
    data = request.get_json()
    print(data)
    print(type(data))
    lecturaTecladoII.main(data['tecla'])
    return jsonify({"status": "success", "received":data})

if __name__ == "__main__":
    # debug=True es util durante el desarrollo.
    # En un entorno real de produccion no se recomienda.
    app.run(host="0.0.0.0", port=5000, debug=True)