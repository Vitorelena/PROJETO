from ... import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    tipo_usuario = db.Column(db.Integer)
    login = db.Column(db.String(20))
    senha = db.Column(db.String(255))

    __mapper_args__={
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo_usuario
    }
    def __repr__(self):
        return f"<User id={self.id}, nome='{self.nome}', cpf='{self.cpf}', tipo_usuario={self.tipo_usuario}>" #só em fase de teste
    def gerar_relatorio(self):
        relatorio = f"------ RELATÓRIO ------\n"
        relatorio += f"Id: {self.id}\n"
        relatorio += f"Nome: {self.nome}\n"
        if self.tipo_usuario == 2:
            relatorio += f"Tipo de Usuario: Cliente"
        elif self.tipo_usuario >= 3:
            relatorio += f"Tipo de Usuario: Funcionário"
        return relatorio
    
