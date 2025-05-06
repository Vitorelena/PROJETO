from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from .Funcionario import Funcionario
from ..service.UserDatabaseService import UserDatabaseService

class SubGerente(Funcionario):
    __maper_args__={
        'polymorfic_identity':5
    }
    def __repr__(self):
        return f"<Funcionario id={self.id}, nome='{self.nome}', cpf='{self.cpf}', matricula='{self.matricula}', numero de vendas = {self.numero_vendas}>" #testar
    def gerar_relatorio(self):
        relatorio = super().gerar_relatorio()
        #exemplo
        relatorio += "\n--- Relatório do SubGerente ---\n"
        relatorio += f"Matrícula: {self.matricula}\n"
        relatorio += f"Numero de vendas: {self.numero_vendas}\n"
        return relatorio
    def fazer_venda(self):
        #colocar o codigo da venda 
        if UserDatabaseService.funcionario_fez_venda(self.id):
            print(f"Venda realizada pelo subgerente {self.nome}, usuario {self.id}")
            return (True)
        else:
            print("Falha em registrar a venda")
        return 
    def ver_estoque(self):
        return
    def editar_estoque(self):
        return
    