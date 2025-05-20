from website.model.Produtos.Produto import Produto
from ... import db

class Equipamentos(Produto):
    tipo = db.Column(db.String(50))  
    marca = db.Column(db.String(30))

    __mapper_args__ = {
        'polymorphic_identity': '4'
    }
    tipo_equipamento = db.Column(db.String(50))
    marca = db.Column(db.String(30))
    def __init__(self,*args,tipo_equipamento = None, marca = None,**kwargs):
        super().__init__(*args,**kwargs)
        self.tipo_equipamento = tipo_equipamento
        self.marca = marca

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTipo: {self.tipo}\nMarca: {self.marca}"