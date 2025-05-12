from . import Produto
from ... import db

class Calcados(Produto):
    numero = db.Column(db.String(5))
    cor = db.Column(db.String(20))
    material = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_identity': 3
    }

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTamanho: {self.numero}\nCor: {self.cor}\nMaterial: {self.material}"
