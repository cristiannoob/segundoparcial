from flask import Flask, jsonify, json
from config.db import db, ma, app
from api.viaje import Viaje, ruta_viaje
from api.Registro import Registro, ruta_registro
from api.pasajero import Pasajero, ruta_pasajeros
from api.pago import Pago, ruta_pagos
from api.vehiculo import Vehiculo, ruta_vehiculos

app.register_blueprint(ruta_pasajeros, url_prefix="/api")
app.register_blueprint(ruta_registro, url_prefix="/api")
app.register_blueprint(ruta_viaje, url_prefix="/api")
app.register_blueprint(ruta_pagos, url_prefix="/api")
app.register_blueprint(ruta_vehiculos, url_prefix="/api")

@app.route("/")
def index():
    return "Hola Mundo"

@app.route('/trestablas', methods=['GET'])
def trestablas():
    datos = {}
    resultado = db.session.query(Registro, Viaje, Pasajero).\
        select_from(Registro).join(Viaje).join(Pasajero).all()
    i=0
    for Registro, Viaje, Pasajero in resultado:
        i+=1
        datos[i]={
            'registro':Registro.id,
            'viaje': Viaje.id,
            'pasajero': Pasajero.id
        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")