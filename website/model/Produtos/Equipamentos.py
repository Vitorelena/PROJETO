from . import Produto
from ... import db

class Equipamentos(Produto):
    tipo = db.Column(db.String(50))  
    marca = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_identity': 4
    }

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTipo: {self.tipo}\nMarca: {self.marca}"