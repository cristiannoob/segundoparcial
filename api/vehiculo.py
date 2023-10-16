from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import Vehiculo, VehiculosSchema

ruta_vehiculos = Blueprint("ruta_vehiculos", __name__)

Vehiculo_schema = VehiculosSchema()
Vehiculos_schema = VehiculosSchema(many=True)

@ruta_vehiculos.route("/vehiculos", methods=["GET"])
def vehiculo():
    resultall = Vehiculo.query.all()  
    resultado_vehiculo = Vehiculos_schema.dump(resultall)
    return jsonify(resultado_vehiculo)


@ruta_vehiculos.route("/savevehiculos", methods=["POST"])
def savevehiculos():
    origen = request.json["origen"]
    destino = request.json["destino"]
    preferencias = request.json["preferencias"]
    new_vehiculo = Vehiculo(
        origen,
        destino,
        preferencias
    )
    db.session.add(new_vehiculo)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_vehiculos.route("/updatevehiculo", methods=["PUT"])
def Updatevehiculo():
    id = request.json["id"]
    origen = request.json["origen"]
    destino = request.json["destino"]
    preferencias = request.json["preferencias"]
    vehiculo = Vehiculo.query.get(id)
    if vehiculo:
        print(vehiculo)
        vehiculo.id = id
        vehiculo.origen = origen
        vehiculo.destino = destino
        vehiculo.preferencias = preferencias
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_vehiculos.route("/deletevehiculo/<id>", methods=["DELETE"])
def eliminar(id):
    vehiculo = Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify(
        Vehiculo_schema.dump(vehiculo),
    )