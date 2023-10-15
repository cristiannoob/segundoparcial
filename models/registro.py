from config.db import db, ma, app

class Registro(db.Model):
    __tablename__ = "tablaRegistro"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    

    def __init__ (self, nombre, correo, edad) :
        self.nombre = nombre
        self.correo = correo

with app.app_context():
    db.create_all()


class RegistrosSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre",
            "correo",
            "edad",
        )