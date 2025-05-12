from ... import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .User import User

class Funcionario(User):
    __mapper_args__={
        'polymorphic_identity': 3
    }
    matricula = db.Column(db.String(20))
    nivel = db.Column(db.Integer)
    numero_vendas = db.Column(db.Integer)

    def __repr__(self):
        return f"<Funcionario id={self.id}, nome='{self.nome}', cpf='{self.cpf}', matricula='{self.matricula}', numero de vendas = {self.numero_vendas}>" #testar
    def gerar_relatorio(self):
        relatorio = super().gerar_relatorio()
        relatorio += "\n--- Sessão do Funcionário ---\n"
        relatorio += f"Matrícula: {self.matricula}\n"
        relatorio += f"Numero de vendas: {self.numero_vendas}\n"
        return relatorio
    def fazer_venda(self):
        return 
    def ver_estoque(self):
        return
    def editar_estoque(self):
        return
     