from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
import os

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Basic Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Mail Config
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'solutioninfotech76@gmail.com'  # your Gmail
    app.config['MAIL_PASSWORD'] = 'your_app_password_here'        # your Gmail App Password
    app.config['MAIL_DEFAULT_SENDER'] = 'solutioninfotech76@gmail.com'

    # Initialize Extensions
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register Routes
    from app.routes import init_routes
    init_routes(app)

    return app
