from website.model.Produtos.Produto import Produto
from ... import db

class VestuarioFeminino(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '1'
    }
    tamanho_feminino = db.Column(db.String(5))
    tecido_feminino = db.Column(db.String(20))

    def __init__(self,*args,tamanho_feminino = None, tecido_feminino = None ,**kwargs):
        super().__init__(*args, **kwargs)
        self.tamanho_feminino = tamanho_feminino
        self.tecido_feminino = tecido_feminino
    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTamanho: {self.tamanho}\nCor: {self.cor}\nTecido: {self.tecido}"
