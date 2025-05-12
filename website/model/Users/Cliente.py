from ... import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .User import User

class Cliente(User):
    __mapper_args__={
        'polymorphic_identity': 2
    }
    numero_compras = db.Column(db.Integer)
    def __repr__(self):
        return f"<Cliente id={self.id}, nome='{self.nome}', cpf='{self.cpf}', numero de compras = {self.numero_compras}>" #testar
    def gerar_relatorio(self):
        relatorio = super().gerar_relatorio()
        relatorio += "\n--- Sessão do Cliente ---\n"
        relatorio += f"Numero de compras: {self.numero_compras}\n"
        return relatorio
