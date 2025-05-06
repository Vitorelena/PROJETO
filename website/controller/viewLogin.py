from flask import Blueprint,render_template, request, redirect, url_for
from ..service.UserDatabaseService import UserDatabaseService

viewLogin = Blueprint('viewLogin', __name__)

@viewLogin.route('/login', methods=['GET','POST'])
def login_page():
    data = request.form
    print(data)
    return render_template("login.html")
@viewLogin.route('/logout')
def logout():
    return "<p>Logout</p>"