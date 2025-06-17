from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager, current_user
from flask_mail import Mail
from dotenv import load_dotenv

db = SQLAlchemy()
DB_NAME = "database.db"
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SECRET_KEY']='trabalhodepoo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = 'trabalhodepoogrupo13@gmail.com'

    mail.init_app(app)
    db.init_app(app)

    global login_manager # Indica que você está usando a variável global login_manager
    login_manager.init_app(app)
    login_manager.login_view = 'viewLogin.login_page'

    from .controller.viewHome import views
    from .controller.viewLogin import viewLogin
    from .controller.viewSignup import viewSign
    from .controller.viewProduct import view_product
    from .controller.viewVenda import view_venda
    from .controller.emailController import emailc
    from .controller.clienteController import viewcliente

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(viewLogin, url_prefix='/login')
    app.register_blueprint(viewSign, url_prefix='/sign')
    app.register_blueprint(view_product, url_prefix='/prod')
    app.register_blueprint(view_venda,url_prefix='/venda')
    app.register_blueprint(emailc, url_prefix='/email')
    app.register_blueprint(viewcliente, url_prefix='/cliente')


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
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            print("Tentando criar o banco de dados e as tabelas...")
            db.create_all()
        print('Created Database!')