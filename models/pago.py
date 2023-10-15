from config.db import db, ma, app

class Pago(db.Model):
    __tablename__ = "tablaPago"

    id = db.Column(db.Integer, primary_key=True)
    tipo_pago= db.Column(db.String(50))
    cantidad = db.Column(db.Integer(50))

    def __init__ (self, tipo_pago, cantidad) :
        self.tipo_pago = tipo_pago
        self.cantidad = cantidad

with app.app_context():
    db.create_all()


class PagosSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_viaje",
        )