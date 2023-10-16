from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reporte import Reporte, ReportesSchema

ruta_reporte = Blueprint("ruta_reporte", __name__)

reporte_schema = ReportesSchema()
reporte_schema = ReportesSchema(many=True)

@ruta_reporte.route("/reporte", methods=["GET"])
def reporte():
    resultall = reporte.query.all()  
    resultado_reporte = reporte_schema.dump(resultall)
    return jsonify(resultado_reporte)


@ruta_reporte.route("/savereporte", methods=["POST"])
def save():
    id = request.json["id"]
    viaje_realizado = request.json["viaje_realizado"]
    ingresos = request.json["ingresos"]
    new_reporte = Reporte(
        id,
        viaje_realizado,
        ingresos
    )
    db.session.add(new_reporte)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_reporte.route("/updatereporte", methods=["PUT"])
def Update():
    id = request.json["id"]
    viaje_realizado = request.json["viaje_realizado"]
    ingresos = request.json["ingresos"]
    reporte = Reporte.query.get(id)
    if reporte:
        print(reporte)
        reporte.id = id
        reporte.viaje_realizado = viaje_realizado
        ruta_reporte.ingresos = ingresos
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_reporte.route("/deleteregistro/<id>", methods=["DELETE"])
def eliminar(id):
    reporte = Reporte.query.get(id)
    db.session.delete(reporte)
    db.session.commit()
    return jsonify(
        reporte_schema.dump(reporte),
    )