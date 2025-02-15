from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import abc_route, call_ai