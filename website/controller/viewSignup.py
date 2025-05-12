from flask import Blueprint,render_template, request, redirect, url_for
from ..service.UserDatabaseService import UserDatabaseService
from werkzeug.security import generate_password_hash

viewSign = Blueprint('viewSign', __name__)

@viewSign.route('/sign-up',  methods=['GET','POST'])
def sign_up():
   if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        login = request.form.get('login')
        senhainsegura = request.form.get('senha')
        tipo_usuario = int(request.form.get('tipo_usuario'))
        senha = generate_password_hash(senhainsegura)
        if tipo_usuario == 2:
            novo_cliente = UserDatabaseService.adicionar_cliente(nome = nome, cpf = cpf, login = login, senha = senha)
            if novo_cliente:
                print(f"Cliente {nome} cadastrado com ID:{novo_cliente.id}")
                return redirect(url_for('view.home'))
            else:
                print("Erro ao cadastrar o cliente")
        elif tipo_usuario == 3:
            nivel_funcionario = int(request.form.get('nivel_funcionario'))
            matricula = request.form.get('matricula')
            if nivel_funcionario == 1:
                novo_funcionario = UserDatabaseService.adicionar_staff(nome = nome, cpf= cpf, login = login, senha=senha, matricula=matricula)
            elif nivel_funcionario == 2:
                novo_funcionario = UserDatabaseService.adicionar_subgerente(nome = nome, cpf= cpf, login = login, senha=senha, matricula=matricula)
            elif nivel_funcionario == 3:
                novo_funcionario = UserDatabaseService.adicionar_gerente(nome = nome, cpf= cpf, login = login, senha=senha, matricula=matricula)
            else:
                print("Nivel inválido")
            if novo_funcionario:
                print(f"Funcionario {nome} cadastrado com nivel {nivel_funcionario}")
            else:
                print("Erro ao cadastrar nivel")
        else:
            pass

   return render_template("sign_up.html")