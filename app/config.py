import os

class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads'),

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'solutioninfotech76@gmail.com'        # use an app password (see below)
    MAIL_PASSWORD = 'your_app_password_here'      # generated from Gmail (not your Gmail login password)
    MAIL_DEFAULT_SENDER = 'solutioninfotech76@gmail.com'