from .. import db
from ..model.User import User
from ..model.Funcionario import Funcionario
from ..model.Cliente import Cliente

class UserDatabaseService:
    @staticmethod
    def adicionar_funcionario(nome, cpf, login, senha, matricula):
        novo_funcionario = Funcionario(nome = nome, cpf = cpf, tipo_usuario = 3, login = login, senha = senha, matricula = matricula, numero_vendas = 0)
        db.session.add(novo_funcionario)
        db.session.commit()
        return novo_funcionario
    
    @staticmethod
    def adicionar_cliente(nome, cpf, login, senha):
        novo_cliente = Cliente(nome = nome, cpf = cpf, tipo_usuario = 2, login = login, senha = senha, numero_compras = 0)
        db.session.add(novo_cliente)
        db.session.commit()
        return novo_cliente
    
    @staticmethod
    def obter_usuario_por_id(usuario_id):
        return User.query.get(usuario_id)
    
    @staticmethod
    def listar_usuarios():
        return User.query.all()
    
    @staticmethod
    def listar_funcionarios():
        return Funcionario.query.all()
    
    @staticmethod
    def listar_clientes():
        return Cliente.query.all()
    
    @staticmethod
    def editar_funcionario(usuario_id , nome=None, cpf=None, login=None, senha=None, matricula=None, numero_vendas=None):
        funcionario = Funcionario.query.get(usuario_id)
        if funcionario and funcionario.tipo_usuario == 3:
            if nome:
                funcionario.nome = nome
            if cpf:
                funcionario.cpf = cpf
            if login:
                funcionario.login = login
            if senha:
                funcionario.senha = senha
            if matricula:
                funcionario.matricula = matricula
            if numero_vendas is not None:
                funcionario.numero_vendas = numero_vendas
            db.session.commit()
            return(True)
        return(False)
    
    @staticmethod 
    def funcionario_fez_venda(usuario_id):
        funcionario = Funcionario.query.get(usuario_id)
        if funcionario and funcionario.tipo_usuario == 3:
            funcionario.numero_vendas += 1
            db.session.commit
            return(True)
        return(False)
    
    @staticmethod
    def editar_cliente(usuario_id, nome=None, cpf=None, login=None, senha=None, numero_compras=None):
        cliente = Cliente.query.get(usuario_id)
        if cliente and cliente.tipo_usuario == 2:
            if nome:
                cliente.nome = nome
            if cpf:
                cliente.cpf = cpf
            if login:
                cliente.login = login
            if senha:
                cliente.senha = senha
            if numero_compras is not None:
                cliente.numero_compras = numero_compras
            db.session.commit()
            return(True)
        return(False)
    
    @staticmethod
    def cliente_fez_compra(usuario_id):
        cliente = Cliente.query.get(usuario_id)
        if cliente and cliente.tipo_usuario == 2:
            cliente.numero_compras += 1
            db.session.commit()
            return(True)
        return(False)
    
    @staticmethod
    def deletar_usuario(usuario_id):
        usuario = User.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario) 
            db.session.commit()
            return(True)
        return(False)       