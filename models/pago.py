from config.db import db, ma, app

class Pago(db.Model):
    __tablename__ = "tablaPago"

    id = db.Column(db.Integer, primary_key=True)
    tipo_pago= db.Column(db.String(50))
    cantidad = db.Column(db.Integer(50))


with app.app_context():
    db.create_all()


class PagosSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_viaje",
        )