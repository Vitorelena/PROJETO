from .. import db
from ..model.Estoque import Estoque
from ..model.Produtos.Produto import Produto

class EstoqueDatabaseService:

    @staticmethod
    def subtrair_do_estoque(produto_id, quantidade):
        estoque = Estoque.query.filter_by(produto_id = produto_id).first()
        if not estoque:
            return False, "Estoque não encontrado para este produto"
        if estoque.quantidade >= quantidade and quantidade > 0:
            estoque.quantidade -= quantidade
            estoque.valor_total -= estoque.produto.preco * quantidade
            db.session.commit()
            EstoqueDatabaseService.atualizar_valor_total_estoque(produto_id) 
            return True, None
        else:
            return False, "Quantidade insuficiente em estoque."
        
    @staticmethod
    def adicionar_ao_estoque(produto_id, quantidade):
        estoque = Estoque.query.filter_by(produto_id=produto_id).first()
        if not estoque:
            return False, "Estoque não encontrado para este produto."
        if quantidade > 0:
            estoque.quantidade += quantidade
            estoque.valor_total += estoque.produto.preco * quantidade
            db.session.commit()
            EstoqueDatabaseService.atualizar_valor_total_estoque(produto_id) 
            return True, None, estoque.quantidade
        else:
            return False, "Quantidade a adicionar deve ser maior que zero."
        
    @staticmethod
    def get_estoque_por_produto_id(produto_id):
        return Estoque.query.filter_by(produto_id=produto_id).first()

    @staticmethod
    def get_todos_itens_estoque():
        return Estoque.query.all()

    @staticmethod
    def atualizar_valor_total_estoque(produto_id):
        estoque = Estoque.query.filter_by(produto_id=produto_id).first()
        produto = Produto.query.get(produto_id)
        if estoque and produto:
            estoque.valor_total = estoque.quantidade * produto.preco
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_valor_total_estoque():
        todos_estoques = Estoque.query.all()
        valor_total_geral = sum(estoque.valor_total for estoque in todos_estoques)
        return valor_total_geral

    @staticmethod
    def excluir_estoque_do_produto(produto_id):
        estoque = Estoque.query.filter_by(produto_id=produto_id).first()
        if estoque:
            db.session.delete(estoque)
            db.session.commit()
            return True
        return False