from flask import Blueprint,render_template, request, redirect, url_for
import folium
from .. import db
from ..model.Loja import Loja
from ..model.Users.Cliente import Cliente
from ..model.Produtos.Produto import Produto
from sqlalchemy.orm import joinedload
from ..service.ProdutoDatabaseService import ProdutoDatabaseService
from flask_login import current_user

views = Blueprint('view', __name__)

@views.route('/teste')
def teste():
    return render_template("layout.html")

@views.route('/', defaults={'categoria_id': None})
@views.route('/categoria/<int:categoria_id>')
def home(categoria_id):
    lojas = Loja.query.all()
    map_center = [-19.92083, -43.93778]
    m = folium.Map(location=map_center, zoom_start=10)

    for loja in lojas:
        folium.Marker(
            location = [loja.latitude, loja.longitude],
            popup=f"<strong>{loja.nome}</strong><br>{loja.endereco}").add_to(m)
    
    map_html = m._repr_html_()

    categoria_templates = {
        1: 'feminino',  # Assumindo que 1 é 'VestuarioFeminino'
        2: 'masculino', # Assumindo que 2 é 'VestuarioMasculino'
        3: 'calcados',   # Assumindo que 3 é 'Calcados'
        4: 'esportivos', # Assumindo que 4 é 'EquipamentosEsportivos'
        5: 'suplementos', # Corresponde ao seu 'Suplementos' com identity 5
        6: 'outros'      # Assumindo que 6 é 'Outros'
    }
    produtos_em_estoque = []
    todos_produtos = ProdutoDatabaseService.get_todos_produtos()
    for produto in todos_produtos:
        produto_com_estoque = db.session.query(Produto).options(joinedload(Produto.estoque)).filter_by(id=produto.id).first()
        if produto_com_estoque and produto_com_estoque.estoque and produto_com_estoque.estoque.quantidade > 0:
            produtos_em_estoque.append(produto_com_estoque)

    if categoria_id and categoria_id in categoria_templates:
        nome_template = categoria_templates[categoria_id] + '.html'
        produtos_categoria = ProdutoDatabaseService.get_produtos_por_categoria(categoria_id)
        produtos_com_estoque_categoria = []
        for produto in produtos_categoria:
            produto_estoque = db.session.query(Produto).options(joinedload(Produto.estoque)).filter_by(id=produto.id).first()
            if produto_estoque:
                produtos_com_estoque_categoria.append(produto_estoque)
        return render_template(nome_template, produtos=produtos_com_estoque_categoria, produtos_estoque_home=produtos_em_estoque)
    else:
        return render_template("home.html", map_html = map_html, produtos_estoque_home=produtos_em_estoque)

@views.route('/home_cliente')
def home_cliente():
    relatorio = current_user.gerar_relatorio()
    return render_template("home_cliente.html", current_user=current_user, relatorio=relatorio)

@views.route('/home_funcionario')
def home_funcionario():
    relatorio = current_user.gerar_relatorio()
    return(render_template("home_funcionario.html",current_user=current_user, relatorio=relatorio))

