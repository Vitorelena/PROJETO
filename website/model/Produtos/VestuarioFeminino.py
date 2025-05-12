from . import Produto
from ... import db

class VestuarioFeminino(Produto):
    tamanho = db.Column(db.String(5))
    cor = db.Column(db.String(20))
    tecido = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_identity': 1
    }

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTamanho: {self.tamanho}\nCor: {self.cor}\nTecido: {self.tecido}"
