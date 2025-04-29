from flask import Blueprint, render_template

views = Blueprint('view1', __name__)

@views.route('/')
def initial():
    return"<h1>Test</h1>"

@views.route('/teste')
def teste():
    return render_template("layout.html")

@views.route('/home')
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
