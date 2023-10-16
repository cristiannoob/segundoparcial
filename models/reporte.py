from config.db import db, ma, app

class Reporte(db.Model):
    __tablename__ = "tablaReporte"

    id = db.Column(db.Integer, primary_key=True)
    viaje_realizados = db.Column(db.String(50))
    ingresos = db.Column(db.String(50))

    def __init__ (self, viaje_realizados, ingresos) :
        self.viaje_realizados = viaje_realizados
        self.ingresos = ingresos

with app.app_context():
    db.create_all()


class ReportesSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "viaje_realizados",
            "ingresos",
        )