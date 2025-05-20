from website.model.Produtos.Produto import Produto
from ... import db

class Suplementos(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '5'
    }
    peso = db.Column(db.String(10))
    sabor = db.Column(db.String(30))
    tipo_suplemento = db.Column(db.String(20))
    def __init__(self,*args,peso = None, sabor = None, tipo_suplemento = None ,**kwargs):
        super().__init__(*args, **kwargs)
        self.peso = peso
        self.sabor = sabor
        self.tipo = tipo_suplemento

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTipo: {self.tipo}\nSabor: {self.sabor}\nQuantidade: {self.peso}"