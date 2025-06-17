from ... import db
from flask_login import UserMixin # Necessário apenas se User for definido aqui
from sqlalchemy.sql import func # Necessário apenas se for usar func.now() ou similar aqui
from .Funcionario import Funcionario

class Ceo(Funcionario):
    __mapper_args__={
        'polymorphic_identity':7
    }
    def __init__(self, *args, **kwargs):
        # CORREÇÃO: Passe 'nivel=4' diretamente para o construtor da classe pai (Funcionario)
        super().__init__(*args, nivel=4, **kwargs)
        
    def __repr__(self):
        # CORREÇÃO: Mude a representação para refletir a classe 'Ceo'
        return f"<Ceo id={self.id}, nome='{self.nome}', cpf='{self.cpf}', matricula='{self.matricula}', numero de vendas = {self.numero_vendas}, nivel {self.nivel}>"

    def gerar_relatorio(self):
       
        relatorio = super().gerar_relatorio()               
        relatorio += "\n--- Relatório do CEO ---\n"
        relatorio += f"Cargo: Ceo"        
        return relatorio