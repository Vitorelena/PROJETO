from ... import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .Funcionario import Funcionario


class SubGerente(Funcionario):
    __mapper_args__={
        'polymorphic_identity':5
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nivel = 2

    def __repr__(self):
        return f"<Funcionario id={self.id}, nome='{self.nome}', cpf='{self.cpf}', matricula='{self.matricula}', numero de vendas = {self.numero_vendas}>" #testar
    def gerar_relatorio(self):
        relatorio = super().gerar_relatorio()
        #exemplo
        relatorio += "\n--- Relatório do SubGerente ---\n"
        relatorio += f"Cargo: Subgerente"
        return relatorio
    def fazer_venda(self):
        return
        #colocar o codigo da venda 
    def ver_estoque(self):
        return
    def editar_estoque(self):
        return
    