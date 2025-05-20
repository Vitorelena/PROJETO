from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='trabalhodepoo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    global login_manager # Indica que você está usando a variável global login_manager
    login_manager.init_app(app)
    login_manager.login_view = 'viewLogin.login_page'

    from .controller.viewHome import views
    from .controller.viewLogin import viewLogin
    from .controller.viewSignup import viewSign
    from .controller.viewProduct import view_product
    from .controller.viewVenda import view_venda


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(viewLogin, url_prefix='/')
    app.register_blueprint(viewSign, url_prefix='/')
    app.register_blueprint(view_product, url_prefix='/')
    app.register_blueprint(view_venda,url_prefix='/')


    from .model.Produtos.VestuarioFeminino import VestuarioFeminino
    from .model.Produtos.VestuarioMasculino import VestuarioMasculino
    from .model.Produtos.Calcados import Calcados
    from .model.Produtos.Suplementos import Suplementos
    from .model.Produtos.Equipamentos import Equipamentos
    from .model.Produtos.Outros import Outros
    from .model.Produtos.Produto import Produto  # Importe Produto AQUI

    from .model.Loja import Loja
    from .model.Users.User import User
    # ... outros modelos de usuário ...

    from .model.Vendas.Venda import Venda
    from .model.Vendas.ItemVendido import ItemVendido


    from .model.Users.User import User
    from . import login_manager # Isso aqui não é necessário, já temos a global
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            print("Tentando criar o banco de dados e as tabelas...")
            db.create_all()
        print('Created Database!')