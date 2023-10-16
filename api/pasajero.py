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
    id_viaje = request.json["id_viaje"]
    nombre = request.json["nombre"]
    correo = request.json["correo"]
    new_pasajero = Pasajero(
        id_viaje,
        nombre,
        correo
    )
    db.session.add(new_pasajero)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_pasajeros.route("/updatepasajero", methods=["PUT"])
def Update():
    id = request.json["id"]
    id_viaje = request.json["idviaje"]
    nombre = request,json["nombre"]
    correo = request.json["correo"]
    pasajero = Pasajero.query.get(id)
    if pasajero:
        print(pasajero)
        pasajero.id = id
        pasajero.idviaje = id_viaje
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