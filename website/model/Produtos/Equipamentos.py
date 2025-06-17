from website.model.Produtos.Produto import Produto
from ... import db

class Equipamentos(Produto):
    __mapper_args__ = {
        'polymorphic_identity': '4' # Mantenha como string
    }
    
    # Colunas específicas para Equipamentos
    # 'tipo' já existe na classe base Produto, então não redefina aqui.
    # O 'tipo_equipamento' é a coluna específica para o tipo detalhado do equipamento.
    tipo_equipamento = db.Column(db.String(50)) # <--- ADICIONE ESTA LINHA DE VOLTA!
    marca = db.Column(db.String(30)) # A marca é específica de Equipamentos

    def __init__(self, *args, tipo_equipamento=None, marca=None, **kwargs):
        # Passar os atributos específicos para o construtor da classe pai
        # 'tipo_equipamento' é o nome da coluna no DB e o atributo Python que queremos.
        # 'marca' é o nome da coluna no DB e o atributo Python que queremos.
        super().__init__(*args, tipo_equipamento=tipo_equipamento, marca=marca, **kwargs)
        # Não precisa de self.tipo_equipamento = tipo_equipamento aqui, pois super().__init__ já cuida.

    def gerar_relatorio(self):
        base = super().gerar_relatorio()
        # Use o atributo com o nome da coluna específica
        return f"{base}\nTipo: {self.tipo_equipamento}\nMarca: {self.marca}"