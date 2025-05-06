from flask import Blueprint,render_template, request, redirect, url_for
from ..service.UserDatabaseService import UserDatabaseService

viewSign = Blueprint('viewSign', __name__)

@viewSign.route('/sign-up',  methods=['GET','POST'])
def sign_up():
   if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        login = request.form.get('login')
        senha = request.form.get('senha')
        tipo_usuario = int(request.form.get('tipo_usuario'))
        if tipo_usuario == 2:
            novo_cliente = UserDatabaseService.adicionar_cliente(nome = nome, cpf = cpf, login = login, senha = senha)
            if novo_cliente:
                print(f"Cliente {nome} cadastrado com ID:{novo_cliente.id}")
                return redirect(url_for('view.home'))
            else:
                print("Erro ao cadastrar o cliente")
        elif tipo_usuario == 3:
            matricula = request.form.get('matricula')
            novo_funcionario = UserDatabaseService.adicionar_funcionario(nome = nome, cpf = cpf, login = login, senha = senha, matricula= matricula)
            if novo_funcionario:
                print(f"Funcionario {nome} cadastrado com ID:{novo_funcionario.id}")
                return redirect(url_for('view.home'))
            else:
                print("Erro ao cadastrar o funcionario")
        else:
            pass

   return render_template("sign_up.html")