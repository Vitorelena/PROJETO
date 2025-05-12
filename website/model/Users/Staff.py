from ... import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .Funcionario import Funcionario

class Staff(Funcionario):
    __mapper_args__={
        'polymorphic_identity':4
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nivel = 1

    def __repr__(self):
        return f"<Funcionario id={self.id}, nome='{self.nome}', cpf='{self.cpf}', matricula='{self.matricula}', numero de vendas = {self.numero_vendas}, nivel {self.nivel}>" #testar
    def gerar_relatorio(self):
        relatorio = super().gerar_relatorio()
        relatorio += "\n--- Relatório do Staff ---\n"
        relatorio += f"Cargo: Staff"
        return relatorio
    def fazer_venda(self):
        return 
    def ver_estoque(self):
        return
    def editar_estoque(self):
        return
    