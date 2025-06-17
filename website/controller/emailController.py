from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from .viewVenda import obter_carrinho
import random
import string
from website import mail
from flask_mail import Message
from datetime import datetime, timedelta
from ..model.Vendas.Venda import Venda
from ..model.Vendas.ItemVendido import ItemVendido
from ..service.ProdutoDatabaseService import ProdutoDatabaseService
from website import db
from ..service.UserDatabaseService import UserDatabaseService
emailc = Blueprint('emailc', __name__)

def gerar_codigo(tam=6):
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=tam))

def enviar_codigo(email_dest, codigo):
    try:
        msg = Message(
            subject="Código de Confirmação da Compra",
            recipients=[email_dest],
            body=f"Seu código de confirmação é: {codigo}"
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return False

@emailc.route('/enviar_codigo', methods=['POST'])
def enviar_codigo_route():
    email = request.form.get('email')
    if not email:
        flash('Email não fornecido.', 'warning')
        return redirect(url_for('view_venda.finalizar_venda'))

    codigo = gerar_codigo()
    session['codigo_confirmacao'] = codigo
    session['email_confirmacao'] = email

    sucesso = enviar_codigo(email, codigo)
    if sucesso:
        flash('Código enviado para seu email.', 'info')
        return redirect(url_for('emailc.validar_codigo'))
    else:
        flash('Erro ao enviar o código, tente novamente.', 'danger')
        return redirect(url_for('view_venda.finalizar_venda'))

@emailc.route('/pedir_email', methods=['GET', 'POST'])
@login_required
def pedir_email():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            flash('Informe um email válido.', 'warning')
            return render_template('pedir_email.html')

        # Determinar cliente_id e funcionario_id seguindo a regra:
        cliente_id = None
        funcionario_id = None

        if current_user.tipo_usuario == 2:
            cliente_id = current_user.id
        elif current_user.tipo_usuario >= 3:
            cliente_id = request.form.get('cliente_id')  # Você precisa garantir que esse campo esteja no formulário!
            funcionario_id = current_user.id

        carrinho = obter_carrinho()
        itens_carrinho = carrinho.obter_itens()
        if not itens_carrinho:
            flash('Seu carrinho está vazio.', 'warning')
            return redirect(url_for('view_venda.carrinho'))

        # Salvar os dados da venda pendente na sessão
        session['venda_pendente'] = {
            'cliente_id': cliente_id,
            'funcionario_id': funcionario_id,
            'itens': itens_carrinho,
            'email': email
        }

        codigo = gerar_codigo()
        sucesso = enviar_codigo(email, codigo)
        if not sucesso:
            flash('Erro ao enviar email. Tente novamente.', 'danger')
            return render_template('pedir_email.html')

        session['codigo_confirmacao'] = codigo
        session['codigo_expira_em'] = (datetime.utcnow() + timedelta(minutes=20)).isoformat()

        flash('Código enviado para seu email.', 'info')
        return redirect(url_for('emailc.validar_codigo'))

    # GET
    user_service = UserDatabaseService()
    clientes = None
    if current_user.tipo_usuario >= 3:
        clientes = user_service.listar_clientes()
    return render_template('pedir_email.html', clientes=clientes)


@emailc.route('/validar_codigo', methods=['GET', 'POST'])
@login_required
def validar_codigo():
    if request.method == 'POST':
        codigo_digitado = request.form.get('codigo')
        codigo_armazenado = session.get('codigo_confirmacao')
        
        expira_em_str = session.get('codigo_expira_em')
        if expira_em_str:
            from datetime import datetime
            expira_em = datetime.fromisoformat(expira_em_str)
            if datetime.utcnow() > expira_em:
                session.pop('codigo_confirmacao', None)
                session.pop('codigo_expira_em', None)
                flash('Código expirado. Solicite um novo.', 'warning')
                return redirect(url_for('emailc.pedir_email'))
        if codigo_digitado and codigo_digitado.upper() == codigo_armazenado:
            # Código correto: salvar venda no banco usando venda_pendente
            dados_venda = session.get('venda_pendente')
            if not dados_venda:
                flash('Dados da venda não encontrados. Por favor, refaça o processo.', 'danger')
                return redirect(url_for('view_venda.carrinho'))

            produto_service = ProdutoDatabaseService()
            user_service = UserDatabaseService()

            nova_venda = Venda(
                data_venda=datetime.utcnow(),
                cliente_id=dados_venda['cliente_id'],
                funcionario_id=dados_venda.get('funcionario_id')
            )
            db.session.add(nova_venda)
            db.session.flush()

            # Adiciona os itens da venda
            for produto_id, quantidade in dados_venda['itens'].items():
                produto = produto_service.get_produto_por_id(int(produto_id))
                if produto:
                    item_vendido = ItemVendido(
                        venda_id=nova_venda.id,
                        produto_id=produto.id,
                        quantidade=quantidade,
                        preco_unitario=produto.preco
                    )
                    db.session.add(item_vendido)
                    produto.estoque.quantidade -= quantidade

            try:
                db.session.commit()
                session.pop('venda_pendente', None)
                session.pop('codigo_confirmacao', None)
                session.pop('email_confirmacao', None)
                session.pop('carrinho', None)

                user_service.cliente_fez_compra(int(dados_venda['cliente_id']))
                if dados_venda.get('funcionario_id'):
                    user_service.funcionario_fez_venda(dados_venda['funcionario_id'])

                flash('Compra confirmada com sucesso!', 'success')
                return redirect(url_for('view_venda.compra_realizada'))

            except Exception as e:
                db.session.rollback()
                print(f"Erro ao salvar a venda: {e}")
                flash('Erro ao confirmar a compra, tente novamente.', 'danger')
                return redirect(url_for('emailc.validar_codigo'))
        else:
            flash('Código inválido. Tente novamente.', 'danger')

    return render_template('validar_codigo.html')