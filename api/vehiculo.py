from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import Vehiculo, VehiculosSchema

ruta_vehiculos = Blueprint("ruta_vehiculos", __name__)

vehiculos_schema = VehiculosSchema()
vehiculos_schema = VehiculosSchema(many=True)

@ruta_vehiculos.route("/vehiculos", methods=["GET"])
def vehiculos():
    resultall = vehiculos.query.all()  # Select * from Clientes
    resultado_vehiculo = vehiculos_schema.dump(resultall)
    return jsonify(resultado_vehiculo)


@ruta_vehiculos.route("/savevehiculos", methods=["POST"])
def save():
    id = request.json["id"]
    origen = request.json["origen_i"]
    destino = request.json["destino_f"]
    new_vehiculo = Vehiculo(
        id,
        origen,
        destino,
    )
    db.session.add(new_vehiculo)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_vehiculos.route("/updatevehiculo", methods=["PUT"])
def Update():
    id = request.json["id"]
    origen = request.json["origen_i"]
    destino = request.json["destino_f"]
    vehiculo = Vehiculo.query.get(id)
    if vehiculo:
        print(vehiculo)
        vehiculo.id = id
        vehiculo.origen_i = origen
        ruta_vehiculos.cantidadpago = destino
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_vehiculos.route("/deletevehiculo/<id>", methods=["DELETE"])
def eliminar(id):
    pasajero = Vehiculo.query.get(id)
    db.session.delete(vehiculos)
    db.session.commit()
    return jsonify(
        vehiculos_schema.dump(vehiculos),
    )