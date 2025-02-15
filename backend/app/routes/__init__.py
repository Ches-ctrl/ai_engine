from flask import Blueprint

bp = Blueprint('main', __name__)

def init_app(app):
    # Import routes here to avoid circular imports
    from app.routes import abc_route, cv_routes

    app.register_blueprint(bp)
    app.register_blueprint(cv_routes.bp)
