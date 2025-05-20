from website import db
from datetime import datetime 

class Venda(db.Model):
    __tablename__ = 'venda'
    id = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    funcionario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    itens_vendidos = db.relationship('ItemVendido', backref='itens')