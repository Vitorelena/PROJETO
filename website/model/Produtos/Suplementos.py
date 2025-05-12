from . import Produto
from ... import db

class Suplementos(Produto):
    peso = db.Column(db.String(10))  
    sabor = db.Column(db.String(30))
    tipo = db.Column(db.String(30))  
    __mapper_args__ = {
        'polymorphic_identity': 5
    }

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTipo: {self.tipo}\nSabor: {self.sabor}\nQuantidade: {self.peso}"