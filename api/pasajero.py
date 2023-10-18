from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pasajero import Pasajero, PasajerosSchema

ruta_pasajeros = Blueprint("ruta_pasajeros", __name__)

pasajero_schema = PasajerosSchema()
pasajeros_schema = PasajerosSchema(many=True)

@ruta_pasajeros.route("/pasajeros", methods=["GET"])
def pasajero():
    resultall = Pasajero.query.all()  # Select * from Clientes
    resultado_pasajero = pasajeros_schema.dump(resultall)
    return jsonify(resultado_pasajero)


@ruta_pasajeros.route("/savepasajero", methods=["POST"])
def save():
    nombre = request.json["nombre"]
    correo = request.json["correo"]
    new_pasajero = Pasajero(
        nombre,
        correo
    )
    db.session.add(new_pasajero)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_pasajeros.route("/updatepasajero", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["nombre"]
    correo = request.json["correo"]
    pasajero = Pasajero.query.get(id)
    if pasajero:
        print(pasajero)
        pasajero.id = id
        pasajero.nombre = nombre
        pasajero.correo = correo
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_pasajeros.route("/deletepasajero/<id>", methods=["DELETE"])
def eliminar(id):
    pasajero = Pasajero.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(
        pasajero_schema.dump(pasajero),
    )

@app.route('/dostablas', methods=['POST'])
def dostablas():
    datos = {}
    resultado = db.session.query(Pasajero, Viaje ).\
        select_from(Pasajero).join(Viaje).all()
    i=0
    for Pasajero, Viaje in resultado:
        i+=1
        datos[i]={
            'pasajero': Pasajero.id,
            'viaje': Viaje.id         
        }
    return datos