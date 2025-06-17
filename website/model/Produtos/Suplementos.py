from website.model.Produtos.Produto import Produto
from ... import db

class Suplementos(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '5' # Mantenha como string
    }
    peso = db.Column(db.String(10))
    sabor = db.Column(db.String(30))
    # CORREÇÃO: Mantenha o nome do atributo Python igual ao nome da coluna
    tipo_suplemento = db.Column(db.String(20)) 

    # AJUSTE NO CONSTRUTOR
    # Os parâmetros devem ser os nomes que você usou nos campos do formulário HTML
    def __init__(self, *args, peso=None, sabor=None, tipo_suplemento=None, **kwargs):
        # Passar os atributos específicos diretamente para super().__init__()
        # Isso garante que o SQLAlchemy os mapeie corretamente.
        super().__init__(*args, peso=peso, sabor=sabor, tipo_suplemento=tipo_suplemento, **kwargs)
        # Não há necessidade de self.peso = peso, self.sabor = sabor, self.tipo_suplemento = tipo_suplemento aqui,
        # pois o super().__init__() já lidará com a inicialização das colunas mapeadas.

    # AJUSTE NO RELATÓRIO
    # Use o atributo com o nome correto: self.tipo_suplemento
    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nTipo: {self.tipo_suplemento}\nSabor: {self.sabor}\nQuantidade: {self.peso}"