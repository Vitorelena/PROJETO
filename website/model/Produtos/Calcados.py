from website.model.Produtos.Produto import Produto
from ... import db

class Calcados(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '3' # Mantenha como string se categoria no DB for VARCHAR
    }
    numero = db.Column(db.String(5))
    material = db.Column(db.String(20))

    # AQUI: Remova 'cor=None' do parâmetro direto do __init__
    def __init__(self, *args, numero = None, material = None, **kwargs):
        # 1. Extrair 'cor_calcado' de kwargs antes de passá-los para super()
        _cor = kwargs.pop('cor_calcado', None) # Extrai e remove de kwargs
        
        # 2. Chamar o construtor da classe pai, passando 'cor' explicitamente
        super().__init__(*args, cor=_cor, **kwargs) # Passa o valor de cor para Produto.__init__
        
        # 3. Inicializar atributos específicos desta classe
        self.numero = numero
        self.material = material

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        # self.cor será acessado da classe Produto
        return f"{base}\nNúmero: {self.numero}\nCor: {self.cor}\nMaterial: {self.material}"