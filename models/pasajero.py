from config.db import db, ma, app

class Pasajero(db.Model):
    __tablename__ = "tablaPasajero"

    id = db.Column(db.Integer, primary_key=True)
    id_viaje = db.Column(db.Integer, db.ForeignKey("tablaViaje.id"))
    id_registro = db.Column(db.Integer, db.ForeignKey("tablaRegistro.id"))

    def __init__ (self, id_viaje, id_registro) : 
        self.id_viaje = id_viaje
        self.id_registro = id_registro

with app.app_context():
    db.create_all()


class PasajerosSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_viaje",
        )