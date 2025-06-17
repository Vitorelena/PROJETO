from website.model.Produtos.Produto import Produto
from ... import db

class VestuarioMasculino(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '2'
    }
    tamanho = db.Column(db.String(5))
    tecido = db.Column(db.String(20))

    def __init__(self, *args, tamanho_masculino = None, tecido_masculino= None ,**kwargs):
        # 1. Extrair 'cor_vestuario' de kwargs antes de passá-los para super()
        # Assume que o campo de cor para vestuário masculino também é 'cor_vestuario' no formulário
        _cor = kwargs.pop('cor_vestuario', None) 
        
        # 2. Chamar o construtor da classe pai, passando 'cor' explicitamente
        super().__init__(*args, cor=_cor, **kwargs) # Passa o valor de cor para Produto.__init__
        
        # 3. Inicializar atributos específicos desta classe
        self.tamanho = tamanho_masculino
        self.tecido = tecido_masculino
            
    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        # Usando self.tamanho e self.tecido, que são as colunas específicas desta classe
        return f"{base}\nTamanho: {self.tamanho}\nCor: {self.cor}\nTecido: {self.tecido}"