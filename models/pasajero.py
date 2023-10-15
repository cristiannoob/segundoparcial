from config.db import db, ma, app

class Pasajero(db.Model):
    __tablename__ = "tablaPasajero"

    id = db.Column(db.Integer, primary_key=True)
    id_viaje = db.Column(db.Integer(50), db.ForeignKey("tablaViaje.id"))
    id_registro = db.Column(db.Integer(50), db.ForeignKey("tablaRegistro.id"))


with app.app_context():
    db.create_all()


class PasajerosSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_viaje",
        )