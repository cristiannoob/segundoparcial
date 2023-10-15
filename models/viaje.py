from config.db import db, ma, app

class Viaje(db.Model):
    __tablename__ = "tablaViaje"

    id = db.Column(db.Integer, primary_key=True)
    hora_ini = db.Column(db.String(50))
    hora_fin = db.Column(db.String(50))
    ruta = db.Column(db.String(50))


with app.app_context():
    db.create_all()


class ViajesSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "hora_ini",
            "hora_fin",
            "ruta",
        )