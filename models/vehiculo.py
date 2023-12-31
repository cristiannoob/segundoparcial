from config.db import db, ma, app

class Vehiculo(db.Model):
    __tablename__ = "tablaVehiculo"

    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(50))
    destino = db.Column(db.String(50))
    preferencias = db.Column(db.String(50))
    disponibilidad = db.Column(db.String(50))

    def __init__ (self, origen, destino, preferencias, disponibilidad) :
        self.origen = origen
        self.destino = destino
        self.preferencias = preferencias
        self.disponibilidad = disponibilidad
        
with app.app_context():
    db.create_all()


class VehiculosSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "origen",
            "destino",
            "preferencias",
            "disponibilidad",
        )