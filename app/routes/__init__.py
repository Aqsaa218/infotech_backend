from .auth import auth_routes
from .career import career_routes
from .contact import contact_routes

def init_routes(app):
    app.register_blueprint(auth_routes)
    app.register_blueprint(career_routes)
    app.register_blueprint(contact_routes)
