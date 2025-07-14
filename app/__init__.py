from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')  # ✅ define upload folder
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # ✅ create if missing
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from app.routes import init_routes
    init_routes(app)

    return app
