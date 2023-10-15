from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viaje import Viaje, ViajesSchema

ruta_viaje = Blueprint("ruta_viaje", __name__)

viaje_schema = ViajesSchema()
viaje_schema = ViajesSchema(many=True)

@ruta_viaje.route("/viaje", methods=["GET"])
def viaje():
    resultall = Viaje.query.all()  
    resultado_viaje = viaje_schema.dump(resultall)
    return jsonify(resultado_viaje)


@ruta_viaje.route("/saveviaje", methods=["POST"])
def save():
    id = request.json["id"]
    hora_ini = request.json["hora_ini"]
    hora_fin = request.json["hora_fin"]
    ruta = request.json["ruta"]
    new_viaje = Viaje(
        id,
        hora_ini,
        hora_fin,
        ruta                       
    )
    db.session.add(new_viaje)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_viaje.route("/updateviaje", methods=["PUT"])
def Update():
    id = request.json["id"]
    hora_ini = request.json["hora_ini"]
    hora_fin = request.json["hora_fin"]
    ruta = request.json["ruta"]
    viaje = Viaje.query.get(id)
    if viaje:
        print(viaje)
        viaje.id = id
        viaje.hora_ini = hora_ini
        viaje.hora_fin = hora_fin
        viaje.ruta = ruta
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_viaje.route("/deleteviaje/<id>", methods=["DELETE"])
def eliminar(id):
    viaje = Viaje.query.get(id)
    db.session.delete(viaje)
    db.session.commit()
    return jsonify(
        viaje_schema.dump(viaje),
    )