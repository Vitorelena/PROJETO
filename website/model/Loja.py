from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Loja(db.Model):
    __tablename__ = 'loja'
    id = db.Column(db.Integer, primary_key = True)
    endereco = db.Column(db.String(100))
    cnpj = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
   