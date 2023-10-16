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
    tipo_pago = request.json["tipopago"]
    cantidad = request.json["cantidadpago"]
    new_pago = Pago(
        id,
        tipo_pago,
        cantidad,
    )
    db.session.add(new_pago)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_pagos.route("/updatepasajero", methods=["PUT"])
def Update():
    id = request.json["id"]
    tipo_pago = request.json["tipopago"]
    cantidad = request.json["cantidadpago"]
    pasajero = Pago.query.get(id)
    if pagos:
        print(pagos)
        pasajero.id = id
        pasajero.tipopago = tipo_pago
        pasajero.cantidadpago = cantidad
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_pagos.route("/deletepasajero/<id>", methods=["DELETE"])
def eliminar(id):
    pasajero = Pago.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(
        pagos_schema.dump(pasajero),
    )