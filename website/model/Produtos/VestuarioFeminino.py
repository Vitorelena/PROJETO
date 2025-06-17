from website.model.Produtos.Produto import Produto
from ... import db

class VestuarioFeminino(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '1'
    }
    tamanho_feminino = db.Column(db.String(5))
    tecido_feminino = db.Column(db.String(20))

    def __init__(self, *args, tamanho_feminino=None, tecido_feminino=None, **kwargs):
        # 1. Extrair 'cor_vestuario' de kwargs antes de passá-los para super()
        _cor = kwargs.pop('cor_vestuario', None) # Extrai e remove de kwargs
        
        # 2. Chamar o construtor da classe pai, passando 'cor' explicitamente
        super().__init__(*args, cor=_cor, **kwargs) # Passa o valor de cor para Produto.__init__
        
        # 3. Inicializar atributos específicos desta classe
        self.tamanho_feminino = tamanho_feminino
        self.tecido_feminino = tecido_feminino
    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        # CORREÇÃO AQUI: Use os atributos específicos de VestuarioFeminino
        return f"{base}\nTamanho: {self.tamanho_feminino}\nCor: {self.cor}\nTecido: {self.tecido_feminino}"
