from website.model.Produtos.Produto import Produto
from ... import db

class Outros(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '6'
    }
    detalhes = db.Column(db.String(100))
    def __init__(self,*args, detalhes = None ,**kwargs):
        super().__init__(*args, **kwargs)
        self.detalhes = detalhes

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nDetalhes: {self.detalhes}"