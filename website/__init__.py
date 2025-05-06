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

    
    from .controller.viewHome import views
    from .controller.viewLogin import viewLogin
    from .controller.viewSignup import viewSign

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(viewLogin, url_prefix='/')
    app.register_blueprint(viewSign, url_prefix='/')

    from .model.Loja import Loja
    print(Loja)
    from .model.User import User
    from .model.Cliente import Cliente
    from .model.Funcionario import Funcionario
    from .model.Staff import Staff
    from .model.SubGerente import SubGerente
    from .model.Gerente import Gerente
    from .model.Ceo import Ceo
    
    create_database(app)

    return app

def create_database(app):  
     if not path.exists('website/' + DB_NAME):
        with app.app_context():
            print("Tentando criar o banco de dados e as tabelas...")
            db.create_all()
        print('Created Database!')