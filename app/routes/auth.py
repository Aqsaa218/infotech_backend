from flask import Blueprint

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login')
def login():
    return "Login Page"
@auth_routes.route('/')
def home():
    return "🎉 Flask is working, Aqsa!"

