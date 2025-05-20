from website.model.Produtos.Produto import Produto
from ... import db

class VestuarioMasculino(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '2'
    }
    tamanho = db.Column(db.String(5))
    tecido = db.Column(db.String(20))

    def __init__(self,*args,tamanho_masculino = None, tecido_masculino= None ,**kwargs):
        super().__init__(*args, **kwargs)
        self.tamanho = tamanho_masculino
        self.tecido = tecido_masculino  

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTamanho: {self.tamanho}\nCor: {self.cor}\nTecido: {self.tecido}"
