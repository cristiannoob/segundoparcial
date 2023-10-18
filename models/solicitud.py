from config.db import db, ma, app

class Solicitud(db.Model):
    __tablename__ = "tablaSolicitud"

    id = db.Column(db.Integer, primary_key=True)
    id_pasajero = db.Column(db.Integer, db.ForeignKey("tablaPasajero.id"))
    id_vehiculo = db.Column(db.Integer, db.ForeignKey("tablaVehiculo.id"))

    def __init__ (self, id_pasajero, id_vehiculo) :
        self.id_pasajero = id_pasajero
        self.id_vehiculo = id_vehiculo
        
        
with app.app_context():
    db.create_all()


class SolicitudesSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_pasajero",
            "id_vehiculo",
        )