from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/movil2parcial"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = "12345"

db = SQLAlchemy(app)

ma = Marshmallow(app) 