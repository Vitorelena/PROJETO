from flask import Blueprint,render_template, request, redirect, url_for
from ..service.UserDatabaseService import UserDatabaseService

views = Blueprint('view', __name__)

@views.route('/teste')
def teste():
    return render_template("layout.html")

@views.route('/')
def home():
    return render_template("home.html")




