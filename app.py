from flask import Flask, jsonify, json
from config.db import db, ma, app
from api.viaje import Viaje, ruta_viaje
from api.pasajero import Pasajero, ruta_pasajeros
from api.pago import Pago, ruta_pagos
from api.vehiculo import Vehiculo, ruta_vehiculos
from api.reporte import Reporte, ruta_reporte

app.register_blueprint(ruta_pasajeros, url_prefix="/api")
app.register_blueprint(ruta_viaje, url_prefix="/api")
app.register_blueprint(ruta_pagos, url_prefix="/api")
app.register_blueprint(ruta_vehiculos, url_prefix="/api")
app.register_blueprint(ruta_reporte, url_prefix="/api")  

@app.route("/")
def index():
    return "Hola Mundo"



if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")