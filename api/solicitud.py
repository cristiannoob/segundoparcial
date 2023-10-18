from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.solicitud import Solicitud, SolicitudesSchema

ruta_solicitud = Blueprint("ruta_solicitud", __name__)

solicitud_schema = SolicitudesSchema()
solicitudes_schema = SolicitudesSchema(many=True)

@ruta_solicitud.route("/solicitud", methods=["GET"])
def solicitud():
    resultall = Solicitud.query.all()  
    resultado_solicitud = solicitudes_schema.dump(resultall)
    return jsonify(resultado_solicitud)


@ruta_solicitud.route("/savesolicitud", methods=["POST"])
def savesolicitud():
    id_pasajero = request.json["id_pasajero"]
    id_vehiculo = request.json["id_vehiculo"]
    new_solicitud = Solicitud(
        id_pasajero,
        id_vehiculo
    )
    db.session.add(new_solicitud)
    db.session.commit()
    return "Datos guardado con exito"

@ruta_solicitud.route("/updatesolicitud", methods=["PUT"])
def Updatesolicitud():
    id = request.json["id"]
    id_pasajero = request.json["id_pasajero"]
    id_vehiculo = request.json["id_vehiculo"]
    solicitud = Solicitud.query.get(id)
    if solicitud:
        print(solicitud)
        solicitud.id = id
        solicitud.id_pasajero = id_pasajero
        solicitud.id_vehiculo = id_vehiculo
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_solicitud.route("/deletesolicitud/<id>", methods=["DELETE"])
def eliminar(id):
    solicitud = Solicitud.query.get(id)
    db.session.delete(solicitud)
    db.session.commit()
    return jsonify(
        solicitud_schema.dump(solicitud),
    )

@app.route('/trestablas', methods=['POST'])
def trestablas():
    datos = {}
    resultado = db.session.query(Pasajero, Vehiculo, Solicitud ).\
        select_from(Pasajero).join(Vehiculo).join(Solicitud).all()
    i=0
    for Pasajero, Vehiculo, Solicitud in resultado:
        i+=1
        datos[i]={
            'pasajero': Pasajero.id,
            'vehiculo': Vehiculo.id,
            'solicitud': Solicitud.id        
        }
    return datos