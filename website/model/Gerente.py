from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .Funcionario import Funcionario

class Gerente(Funcionario):
    __maper_args__={
        'polymorfic_identity':6
    }
    def __repr__(self):
        return f"<Funcionario id={self.id}, nome='{self.nome}', cpf='{self.cpf}', matricula='{self.matricula}', numero de vendas = {self.numero_vendas}>" #testar
    def gerar_relatorio(self):
        relatorio = super().gerar_relatorio()
        relatorio += "\n--- Relatório do Gerente ---\n"
        relatorio += f"Matrícula: {self.matricula}\n"
        relatorio += f"Numero de vendas: {self.numero_vendas}\n"
        return relatorio
    def fazer_venda(self):
        return 
    def ver_estoque(self):
        return
    def editar_estoque(self):
        return
    