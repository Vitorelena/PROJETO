# Em service/ProdutoDatabaseService.py

from .. import db
from ..model.Produtos.Produto import Produto
from ..model.Estoque import Estoque 

# Importe TODAS as suas subclasses de Produto
from ..model.Produtos.VestuarioFeminino import VestuarioFeminino
from ..model.Produtos.VestuarioMasculino import VestuarioMasculino
from ..model.Produtos.Calcados import Calcados
from ..model.Produtos.Suplementos import Suplementos
from ..model.Produtos.Equipamentos import Equipamentos
from ..model.Produtos.Outros import Outros


class ProdutoDatabaseService:
    @staticmethod
    def criar_produto(nome, descricao, preco, codigo_de_barras, imagem_url, categoria_id, **kwargs):
        novo_produto = None
        
        try:
            categoria_id_int = int(categoria_id)
        except (ValueError, TypeError):
            categoria_id_int = 0 

        if categoria_id_int == 1: # Vestuário Feminino
            novo_produto = VestuarioFeminino(
                nome=nome, descricao=descricao, preco=preco, codigo_de_barras=codigo_de_barras,
                imagem_url=imagem_url, categoria=categoria_id,
                tamanho_feminino=kwargs.get('tamanho_vestuario'), # CORRIGIDO: passar 'tamanho_feminino'
                tecido_feminino=kwargs.get('tecido_vestuario'),   # CORRIGIDO: passar 'tecido_feminino'
                cor_vestuario=kwargs.get('cor_vestuario')         # Passar a cor via kwargs para o pop no __init__
            )
        elif categoria_id_int == 2: # Vestuário Masculino
            novo_produto = VestuarioMasculino(
                nome=nome, descricao=descricao, preco=preco, codigo_de_barras=codigo_de_barras,
                imagem_url=imagem_url, categoria=categoria_id,
                tamanho=kwargs.get('tamanho_vestuario'), # OK: passa para 'tamanho' na subclasse
                tecido=kwargs.get('tecido_vestuario'),   # OK: passa para 'tecido' na subclasse
                cor_vestuario=kwargs.get('cor_vestuario') # Passar a cor via kwargs para o pop no __init__
            )
        elif categoria_id_int == 3: # Calçados
            novo_produto = Calcados(
                nome=nome, descricao=descricao, preco=preco, codigo_de_barras=codigo_de_barras,
                imagem_url=imagem_url, categoria=categoria_id,
                numero=kwargs.get('numero_calcado'), 
                material=kwargs.get('material_calcado'),
                cor_calcado=kwargs.get('cor_calcado') # Passar a cor via kwargs para o pop no __init__
            )
        elif categoria_id_int == 4: # Equipamentos esportivos
            novo_produto = Equipamentos(
                nome=nome, descricao=descricao, preco=preco, codigo_de_barras=codigo_de_barras,
                imagem_url=imagem_url, categoria=categoria_id,
                tipo_equipamento=kwargs.get('tipo_equipamento'), # Passar o nome correto para o __init__
                marca_equipamento=kwargs.get('marca_equipamento') # Passar o nome correto para o __init__
            )
        elif categoria_id_int == 5: # Suplementos
            novo_produto = Suplementos(
                nome=nome, descricao=descricao, preco=preco, codigo_de_barras=codigo_de_barras,
                imagem_url=imagem_url, categoria=categoria_id,
                peso=kwargs.get('peso_suplemento'), 
                sabor=kwargs.get('sabor_suplemento'), 
                tipo_suplemento=kwargs.get('tipo_suplemento') # Passar o nome correto para o __init__
            )
        elif categoria_id_int == 6: # Outros
            novo_produto = Outros(
                nome=nome, descricao=descricao, preco=preco, codigo_de_barras=codigo_de_barras,
                imagem_url=imagem_url, categoria=categoria_id,
                detalhes=kwargs.get('detalhes_outros')
            )
        else: # Cria um Produto base se a categoria não corresponder ou for inválida
            # Se 'cor' é um atributo na classe base Produto, passe-o aqui também.
            # Tenta pegar a cor de qualquer um dos campos de cor do formulário
            cor_base = kwargs.get('cor_vestuario') or kwargs.get('cor_calcado')
            novo_produto = Produto(
                nome=nome, descricao=descricao, preco=preco, codigo_de_barras=codigo_de_barras,
                imagem_url=imagem_url, categoria=categoria_id, cor=cor_base
            )
        
        if novo_produto:
            db.session.add(novo_produto)
            db.session.flush()
            db.session.commit()
        return novo_produto

    # ... (métodos get_produto_por_id, get_produto_por_codigo_barras, get_todos_produtos, get_produtos_por_categoria) ...

    # 2. Modificações no ProdutoDatabaseService.atualizar_produto
    @staticmethod
    def atualizar_produto(produto_id, **kwargs):
        produto = Produto.query.get(produto_id)
        if not produto:
            return False
        
        # 1. Atualizar atributos comuns a TODOS os produtos (presentes na classe Produto)
        for attr in ['nome', 'descricao', 'preco', 'codigo_de_barras', 'imagem_url', 'categoria']:
            if attr in kwargs and kwargs[attr] is not None:
                setattr(produto, attr, kwargs[attr])

        # A cor é um atributo da classe base Produto (cor=db.Column(..., nullable=True)).
        # Ela pode vir de 'cor_vestuario' ou 'cor_calcado' no formulário.
        # Pega a cor do kwargs e atribui ao produto base.
        if 'cor_vestuario' in kwargs and kwargs['cor_vestuario'] is not None:
            produto.cor = kwargs['cor_vestuario']
        elif 'cor_calcado' in kwargs and kwargs['cor_calcado'] is not None:
            produto.cor = kwargs['cor_calcado']
        # Se você tiver um campo 'cor' genérico no form para Produtos base, adicione aqui.


        # 2. Atualizar atributos específicos da subclasse (USANDO isinstance)
        # Isso é crucial para garantir que os atributos corretos sejam atualizados.
        if isinstance(produto, VestuarioFeminino):
            if 'tamanho_vestuario' in kwargs and kwargs['tamanho_vestuario'] is not None:
                produto.tamanho_feminino = kwargs['tamanho_vestuario']
            if 'tecido_vestuario' in kwargs and kwargs['tecido_vestuario'] is not None:
                produto.tecido_feminino = kwargs['tecido_vestuario']
        
        elif isinstance(produto, VestuarioMasculino):
            if 'tamanho_vestuario' in kwargs and kwargs['tamanho_vestuario'] is not None:
                produto.tamanho = kwargs['tamanho_vestuario'] # 'tamanho' sem _masculino
            if 'tecido_vestuario' in kwargs and kwargs['tecido_vestuario'] is not None:
                produto.tecido = kwargs['tecido_vestuario'] # 'tecido' sem _masculino

        elif isinstance(produto, Calcados):
            if 'numero_calcado' in kwargs and kwargs['numero_calcado'] is not None:
                produto.numero = kwargs['numero_calcado']
            if 'material_calcado' in kwargs and kwargs['material_calcado'] is not None:
                produto.material = kwargs['material_calcado']
            # Cor já foi tratada acima se for da classe base Produto

        elif isinstance(produto, Equipamentos):
            if 'tipo_equipamento' in kwargs and kwargs['tipo_equipamento'] is not None:
                produto.tipo = kwargs['tipo_equipamento']
            if 'marca_equipamento' in kwargs and kwargs['marca_equipamento'] is not None:
                produto.marca = kwargs['marca_equipamento']

        elif isinstance(produto, Suplementos):
            if 'peso_suplemento' in kwargs and kwargs['peso_suplemento'] is not None:
                produto.peso = kwargs['peso_suplemento']
            if 'sabor_suplemento' in kwargs and kwargs['sabor_suplemento'] is not None:
                produto.sabor = kwargs['sabor_suplemento']
            if 'tipo_suplemento' in kwargs and kwargs['tipo_suplemento'] is not None:
                produto.tipo_suplemento = kwargs['tipo_suplemento']

        elif isinstance(produto, Outros):
            if 'detalhes_outros' in kwargs and kwargs['detalhes_outros'] is not None:
                produto.detalhes = kwargs['detalhes_outros']

        db.session.commit()
        return True
    
    @staticmethod
    def excluir_produto(produto_id):
        produto = Produto.query.get(produto_id)
        if produto:
            db.session.delete(produto)
            db.session.commit() 
            return True
        return False
    
        
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
    def get_nome_por_id(produto_id):
        produto = Produto.query.get(produto_id)
        if produto:
            return produto.nome
        return None