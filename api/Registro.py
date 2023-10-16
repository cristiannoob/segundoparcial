from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.registro import Registro, RegistrosSchema

ruta_registro = Blueprint("ruta_registro", __name__)

registro_schema = RegistrosSchema()
registro_schema = RegistrosSchema(many=True)

@ruta_registro.route("/regitro", methods=["GET"])
def registro():
    resultall = Registro.query.all()  
    resultado_pasajero = registro_schema.dump(resultall)
    return jsonify(resultado_pasajero)


@ruta_registro.route("/saveregistro", methods=["POST"])
def save():
    id = request.json["id"]
    nombre = request.json["nombre"]
    correo = request.json["correo"]
    new_registro = registro(
        id,
        nombre,
        correo
    )
    db.session.add(new_registro)
    db.session.commit()
    return "Datos guardado con exito"


@ruta_registro.route("/updateregistro", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["nombre"]
    correo = request.json["correo"]
    registro = Registro.query.get(id)
    if registro:
        print(registro)
        registro.id = id
        registro.nombre = nombre
        registro.correo = correo
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_registro.route("/deleteregistro/<id>", methods=["DELETE"])
def eliminar(id):
    pasajero = Registro.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(
        registro_schema.dump(pasajero),
    )
