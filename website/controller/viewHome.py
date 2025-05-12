from flask import Blueprint,render_template, request, redirect, url_for
import folium
from ..model.Loja import Loja
from ..model.Users.Cliente import Cliente

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

    if categoria_id:
        produtos = ProdutoDatabaseService.get_produtos_por_categoria(categoria_id)
    else:
        produtos = ProdutoDatabaseService.get_todos_produtos()
    return render_template("home.html", map_html = map_html)

@views.route('/home_cliente')
def home_cliente():
    relatorio = current_user.gerar_relatorio()
    return render_template("home_cliente.html", current_user=current_user, relatorio=relatorio)

@views.route('/home_funcionario')
def home_funcionario():
    relatorio = current_user.gerar_relatorio()
    return(render_template("home_funcionario.html",current_user=current_user, relatorio=relatorio))

