from config.db import db, ma, app

class Pasajero(db.Model):
    __tablename__ = "tablaPasajero"

    id = db.Column(db.Integer, primary_key=True)
    id_viaje = db.Column(db.Integer, db.ForeignKey("tablaViaje.id"))
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))


    def __init__ (self, id_viaje, nombre, correo) : 
        self.id_viaje = id_viaje
        self.nombre = nombre
        self.correo = correo

with app.app_context():
    db.create_all()


class PasajerosSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_viaje",
            "nombre",
            "correo",
        )