from flask import Blueprint, render_template, request, redirect, url_for
from website import db
from ..service.ProdutoDatabaseService import ProdutoDatabaseService
from ..service.EstoqueDatabaseService import EstoqueDatabaseService
from ..model.Produtos.VestuarioFeminino import VestuarioFeminino
from ..model.Produtos.VestuarioMasculino import VestuarioMasculino
from ..model.Produtos.Calcados import Calcados
from ..model.Produtos.Suplementos import Suplementos
from ..model.Produtos.Equipamentos import Equipamentos
from ..model.Produtos.Outros import Outros

view_product = Blueprint('view_product', __name__)
@view_product.route('/criar_produto', methods=['GET', 'POST'])
def criar_produto():
    novo_produto = None
    print(f"Método da requisição: {request.method}")
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        codigo_de_barras = request.form.get('codigo_de_barras')
        imagem_url = request.form.get('imagem_url')
        categoria_id = request.form.get('categoria')
        cor = request.form.get('cor')

        if (categoria_id == '1'):
            tamanho_feminino = request.form.get('tamanho')
            tecido_feminino = request.form.get('tecido')
            novo_produto = VestuarioFeminino(nome = nome, descricao = descricao, preco = preco, codigo_de_barras = codigo_de_barras, imagem_url = imagem_url, categoria = categoria_id, tamanho_feminino = tamanho_feminino, tecido_feminino = tecido_feminino)
        elif (categoria_id== '2' ):
            tamanho_masculino = request.form.get('tamanho')
            tecido_masculino = request.form.get('tecido')
            novo_produto = VestuarioMasculino(nome = nome, descricao = descricao, preco = preco, codigo_de_barras = codigo_de_barras, imagem_url = imagem_url, categoria = categoria_id, tamanho_masculino = tamanho_masculino,tecido_masculino = tecido_masculino)
        elif categoria_id == '3':
            numero = request.form.get('numero')
            material = request.form.get('material')
            novo_produto = Calcados(nome = nome, descricao = descricao, preco = preco, codigo_de_barras = codigo_de_barras, imagem_url = imagem_url, categoria = categoria_id, numero = numero, material = material)
        elif categoria_id == '4':
            tipo_equipamento = request.form.get('tipo')
            marca = request.form.get('marca')
            novo_produto = Equipamentos(nome = nome, descricao = descricao, preco = preco, codigo_de_barras = codigo_de_barras, imagem_url = imagem_url, categoria = categoria_id, tipo_equipamento= tipo_equipamento, marca = marca)
        elif categoria_id == '5':
            peso = request.form.get('peso')
            sabor = request.form.get('sabor')
            tipo_suplemento = request.form.get('tipo')
            novo_produto = Suplementos(nome = nome, descricao = descricao, preco = preco, codigo_de_barras = codigo_de_barras, imagem_url = imagem_url, categoria = categoria_id, peso = peso, sabor = sabor, tipo_suplemento = tipo_suplemento)
        elif categoria_id == '6':
            detalhes = request.form.get('detalhes')
            novo_produto = Outros(nome = nome, descricao = descricao, preco = preco, codigo_de_barras = codigo_de_barras, imagem_url = imagem_url, categoria = categoria_id, detalhes = detalhes)
        else:
            print("Categoria inválida")

        if novo_produto:
            db.session.add(novo_produto)
            db.session.commit()
            return redirect(url_for('view_product.criar_estoque', produto_id=novo_produto.id))
        else:
            print("Nao foi possivel criar o produto")
            return render_template('criar_produto.html', error="Erro ao criar o produto") # Retorna o formulário com erro
    else:
        print("Método não é POST")
        return render_template('criar_produto.html') # Renderiza o formulário para GET

@view_product.route('/criar_estoque/<int:produto_id>', methods=['GET', 'POST'])
def criar_estoque(produto_id):
    produto = ProdutoDatabaseService.get_produto_por_id(produto_id)
    if not produto:
        return "Produto não encontrado.", 404

    if request.method == 'POST':
        quantidade = int(request.form.get('quantidade'))
        valor_total = produto.preco * quantidade

        estoque_criado = EstoqueDatabaseService.criar_estoque(
            produto_id=produto_id,
            quantidade=quantidade,
            valor_total=valor_total
        )

        if estoque_criado is True:
            return redirect(url_for('view.home'))
        else:
            # Trate o erro na criação do estoque (estoque já existe ou outro erro)
            pass

    return render_template('criar_estoque.html', produto_id=produto_id)