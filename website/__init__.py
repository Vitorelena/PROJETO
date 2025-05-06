from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='trabalhodepoo' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    
    from .controller.view import views

    app.register_blueprint(views, url_prefix='/')

    from .model.User import User
    from .model.Cliente import Cliente
    from .model.Funcionario import Funcionario
    from .model.Staff import Staff
    from .model.SubGerente import SubGerente
    from .model.Gerente import Gerente
    from .model.Ceo import Ceo
    from .model.Loja import Loja
    create_database(app)

    return app

def create_database(app):  
     if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')