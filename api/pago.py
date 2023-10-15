from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pago import Pago, PagosSchema

ruta_pagos = Blueprint("ruta_pagos", __name__)

pagos_schema = PagosSchema()
pasajeros_schema = PagosSchema(many=True)

@ruta_pagos.route("/pagos", methods=["GET"])
def pagos():
    resultall = pagos.query.all()  # Select * from Clientes
    resultado_pago = pagos_schema.dump(resultall)
    return jsonify(resultado_pago)


@ruta_pagos.route("/savepagos", methods=["POST"])
def save():
    id = request.json["id"]
    id_viaje = request.json["idviaje"]
    id_registro = request.json["idregistro"]
    new_pasajero = Pasajero(
        id,
        id_viaje,
        id_registro,
    )
    db.session.add(new_pasajero)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_pagos.route("/updatepasajero", methods=["PUT"])
def Update():
    id = request.json["id"]
    id_viaje = request.json["idviaje"]
    id_registro = request.json["idregistro"]
    pasajero = Pasajero.query.get(id)
    if pasajero:
        print(pasajero)
        pasajero.id = id
        pasajero.idviaje = id_viaje
        pasajero.idregistro = id_registro
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_pagos.route("/deletepasajero/<id>", methods=["GET"])
def eliminar(id):
    pasajero = Pasajero.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(
        pasajero_schema.dump(pasajero),
    )