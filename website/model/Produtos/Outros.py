from website.model.Produtos.Produto import Produto
from ... import db

class Outros(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '6' # Mantenha como string se categoria no DB for VARCHAR
    }
    detalhes = db.Column(db.String(100)) # Coluna definida corretamente

    # AQUI: Ajuste o __init__ para passar 'detalhes' para o super()
    def __init__(self, *args, **kwargs): # Remova 'detalhes = None' daqui, ele virá de kwargs
        # 1. Extrair 'detalhes' de kwargs (pois ele é passado assim pelo ProdutoDatabaseService)
        _detalhes = kwargs.pop('detalhes', None) # Extrai e remove de kwargs
        
        # 2. Chamar o construtor da classe pai, passando 'detalhes' explicitamente
        super().__init__(*args, detalhes=_detalhes, **kwargs) # Passa o valor de detalhes para Produto.__init__
        
        # Você não precisa mais de 'self.detalhes = detalhes' aqui,
        # pois ele já foi tratado pelo construtor da classe pai.

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        return f"{base}\nDetalhes: {self.detalhes}"