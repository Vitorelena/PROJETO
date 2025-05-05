from flask import Blueprint,render_template

views = Blueprint('view', __name__)

@views.route('/teste')
def teste():
    return render_template("layout.html")

@views.route('/')
def home():
    return render_template("home.html")
@views.route('/login')
def login():
    return "<p>Login</p>"

@views.route('/logout')
def logout():
    return "<p>Logout</p>"

@views.route('/sign-up')
def sign_up():
    return "<p>Sign-up</p>"

