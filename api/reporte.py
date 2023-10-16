from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reporte import Reporte, ReportesSchema

ruta_reporte = Blueprint("ruta_reporte", __name__)

reporte_schema = ReportesSchema()
reportes_schema = ReportesSchema(many=True)

@ruta_reporte.route("/reporte", methods=["GET"])
def reporte():
    resultall = Reporte.query.all()  
    resultado_reporte = reportes_schema.dump(resultall)
    return jsonify(resultado_reporte)


@ruta_reporte.route("/savereporte", methods=["POST"])
def save():
    viaje_realizados = request.json["viaje_realizados"]
    ingresos = request.json["ingresos"]
    new_reporte = Reporte(
        viaje_realizados,
        ingresos
    )
    db.session.add(new_reporte)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_reporte.route("/updatereporte", methods=["PUT"])
def Update():
    id = request.json["id"]
    viaje_realizados = request.json["viaje_realizados"]
    ingresos = request.json["ingresos"]
    reporte = Reporte.query.get(id)
    if reporte:
        print(reporte)
        reporte.id = id
        reporte.viaje_realizados = viaje_realizados
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