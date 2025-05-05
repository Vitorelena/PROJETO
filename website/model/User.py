from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tableneme__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    tipo_usuario = db.Column(db.Integer)

    __maper_args__={
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo_usuario
    }
    def __repr__(self):
        return f"<User id={self.id}, nome='{self.nome}', cpf='{self.cpf}', tipo_usuario={self.tipo_usuario}>" #só em fase de teste
    def gerar_relatorio(self):
        relatorio = f"Relatorio Generico\n"
        relatorio += f"Id: {self.id}\n"
        relatorio += f"Nome: {self.nome}\n"
        relatorio += f"Tipo de Usuario: {self.tipo_usuario}"
        return relatorio
    
