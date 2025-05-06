from flask import Blueprint,render_template, request

views = Blueprint('view', __name__)

@views.route('/teste')
def teste():
    return render_template("layout.html")

@views.route('/')
def home():
    return render_template("home.html")
@views.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")
@views.route('/logout')
def logout():
    return "<p>Logout</p>"

@views.route('/sign-up',  methods=['GET','POST'])
def sign_up():
   if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        senha = request.form.get('senha')
        tipo_usuario = request.form.get('tipo_usuario')
        if tipo_usuario == 3:
            matricula = request.form.get('matricula')
        else:
            pass

   return render_template("sign_up.html")

