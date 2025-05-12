from . import Produto
from ... import db

class Outros(Produto):
    detalhes = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 6
    }

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nDetalhes: {self.detalhes}"