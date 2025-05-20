from flask import Blueprint, session, render_template, redirect, url_for, request, flash
from ..model.Vendas.CarrinhoDeCompras import CarrinhoDeCompras
from ..service.ProdutoDatabaseService import ProdutoDatabaseService
from ..model.Vendas.Venda import Venda
from ..model.Vendas.ItemVendido import ItemVendido
from website import db
from flask_login import current_user
from datetime import datetime

view_venda = Blueprint('view_venda', __name__)

def obter_carrinho():
    if 'carrinho' not in session:
        session['carrinho'] = CarrinhoDeCompras().itens
    carrinho = CarrinhoDeCompras()
    carrinho.itens = session['carrinho']
    return carrinho

def salvar_carrinho(carrinho):
    session['carrinho'] = carrinho.itens

@view_venda.route('/adicionar_ao_carrinho/<int:produto_id>', methods=['POST'])
def adicionar_ao_carrinho(produto_id):
    carrinho = obter_carrinho()
    quantidade = int(request.form.get('quantidade',1))
    carrinho.adicionar_item(produto_id, quantidade)
    salvar_carrinho(carrinho)
    return redirect(url_for('view_venda.carrinho'))

@view_venda.route('/remover_do_carrinho/<int:produto_id>')
def remover_do_carrinho(produto_id):
    carrinho = obter_carrinho()
    carrinho.remover_item(produto_id)
    salvar_carrinho(carrinho)
    return redirect(url_for('view_venda.carrinho'))

@view_venda.route('/atualziar_quantidade/<int:produto_id>', methods=['POST'])
def atualizar_quantidade(produto_id):
    carrinho = obter_carrinho()
    quantidade = int(request.form.get('quantidade'))
    carrinho.atualizar_quantidade(produto_id, quantidade)
    salvar_carrinho(carrinho)
    return redirect(url_for('view_venda.carrinho'))

@view_venda.route('/carrinho')
def carrinho():
    carrinho = obter_carrinho()
    produtos_no_carrinho = []
    produto_service = ProdutoDatabaseService()
    for produto_id, quantidade in carrinho.obter_itens().items():
        produto = produto_service.get_produto_por_id(int(produto_id))
        if produto:
            produtos_no_carrinho.append({'produto': produto, 'quantidade': quantidade})
    total = carrinho.calcular_total(produto_service)
    return render_template('carrinho.html', carrinho=produtos_no_carrinho, total=total)

@view_venda.route('/finalizar_venda')
def finalizar_venda():
   return carrinho()

@view_venda.route('/processar_venda', methods=['POST'])
def processar_compra():
    carrinho = obter_carrinho()
    produto_service = ProdutoDatabaseService()
    itens_carrinho = carrinho.obter_itens()

    if not itens_carrinho:
        flash('Seu carrinho está vazio.', 'warning')
        return redirect(url_for('view_venda.carrinho'))

    nova_venda = Venda(
        data_venda=datetime.utcnow(),
        cliente_id=current_user.id if current_user.is_authenticated else None,
        # Você pode precisar adicionar lógica para o funcionário responsável
    )
    db.session.add(nova_venda)
    db.session.flush() # Garante que a 'nova_venda.id' seja gerada

    for produto_id, quantidade in itens_carrinho.items():
        produto = produto_service.get_produto_por_id(int(produto_id))
        if produto:
            item_vendido = ItemVendido(
                venda_id=nova_venda.id,
                produto_id=produto.id,
                quantidade=quantidade,
                preco_unitario=produto.preco
            )
            db.session.add(item_vendido)

            # Atualizar o estoque
            produto.estoque.quantidade -= quantidade

    db.session.commit()

    # Limpar o carrinho após a compra
    session.pop('carrinho', None)
    flash('Compra realizada com sucesso!', 'success')
    return redirect(url_for('view_venda.compra_realizada'))

    # Limpar o carrinho após a compra
    session.pop('carrinho', None)
    flash('Compra realizada com sucesso!', 'success')
    return redirect(url_for('view_venda.compra_realizada'))

@view_venda.route('/compra_realizada')
def compra_realizada():
    return render_template('compra_sucesso.html')