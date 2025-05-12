from ... import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .Funcionario import Funcionario

class Gerente(Funcionario):
    __mapper_args__={
        'polymorphic_identity':6
    }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nivel = 3

    def __repr__(self):
        return f"<Funcionario id={self.id}, nome='{self.nome}', cpf='{self.cpf}', matricula='{self.matricula}', numero de vendas = {self.numero_vendas}>" #testar
    def gerar_relatorio(self):
        relatorio = super().gerar_relatorio()
        relatorio += f"Cargo: Gerente"
        return relatorio
    def fazer_venda(self):
        return 
    def ver_estoque(self):
        return
    def editar_estoque(self):
        return
    