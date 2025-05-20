from .. import db
from ..model.Produtos.Produto import Produto
from ..model.Estoque import Estoque

class ProdutoDatabaseService:
    @staticmethod
    def adicionar_produto(nome, preco, codigo_de_barras=None, imagem_url=None, descricao=None, cor = None):
        novo_produto = Produto(
            nome=nome,
            preco=preco,
            codigo_de_barras=codigo_de_barras,
            imagem_url=imagem_url,
            descricao=descricao,
            cor = cor
        )
        db.session.add(novo_produto)
        db.session.flush() # Garante que o ID do produto seja gerado imediatamente
        db.session.commit()
        return novo_produto
    
    @staticmethod
    def get_produto_por_id(produto_id):
        return Produto.query.get(produto_id)

    @staticmethod
    def get_produto_por_codigo_barras(codigo_de_barras):
        return Produto.query.filter_by(codigo_de_barras=codigo_de_barras).first()

    @staticmethod
    def get_todos_produtos():
        return Produto.query.all()
    
    @staticmethod
    def get_produtos_por_categoria(categoria):
        return Produto.query.filter_by(categoria = categoria).all()

    @staticmethod
    def atualizar_produto(produto_id, nome=None, preco=None, codigo_de_barras=None, imagem_url=None, descricao=None):
        produto = Produto.query.get(produto_id)
        if produto:
            if nome:
                produto.nome = nome
            if preco is not None:
                produto.preco = preco
            if codigo_de_barras:
                produto.codigo_de_barras = codigo_de_barras
            if imagem_url:
                produto.imagem_url = imagem_url
            if descricao:
                produto.descricao = descricao
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def excluir_produto(produto_id):
        produto = Produto.query.get(produto_id)
        if produto:
            db.session.delete(produto)
            db.session.commit() 
            return True
        return False