from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pago import Pago, PagosSchema

ruta_pagos = Blueprint("ruta_pagos", __name__)

pago_schema = PagosSchema()
pagos_schema = PagosSchema(many=True)

@ruta_pagos.route("/pagos", methods=["GET"])
def pagos():
    resultall = Pago.query.all() 
    resultado_pago = pagos_schema.dump(resultall)
    return jsonify(resultado_pago)


@ruta_pagos.route("/savepagos", methods=["POST"])
def save():
    tipo_pago = request.json["tipo_pago"]
    cantidad = request.json["cantidad"]
    new_pago = Pago(
        tipo_pago,
        cantidad,
    )
    db.session.add(new_pago)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_pagos.route("/updatepago", methods=["PUT"])
def Update():
    id = request.json["id"]
    tipo_pago = request.json["tipo_pago"]
    cantidad = request.json["cantidad"]
    pago = Pago.query.get(id)
    if pago:
        print(pago)
        pago.id = id
        pago.tipo_pago = tipo_pago
        pago.cantidad= cantidad
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_pagos.route("/deletepago/<id>", methods=["DELETE"])
def eliminar(id):
    pagos = Pago.query.get(id)
    db.session.delete(pagos)
    db.session.commit()
    return jsonify(
        pago_schema.dump(pagos),
    )