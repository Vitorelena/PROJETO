from website.model.Produtos.Produto import Produto
from ... import db

class Calcados(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '3'
    }
    numero = db.Column(db.String(5))
    material = db.Column(db.String(20))

    def __init__(self,*args, numero = None, cor= None,material = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.numero = numero
        self.material = material

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTamanho: {self.numero}\nCor: {self.cor}\nMaterial: {self.material}"
