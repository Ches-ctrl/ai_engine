from flask import Blueprint
from app.routes import bp

@bp.route('/abc_route', methods=['GET'])
def api_endpoint():
    return {
        "message": "abc_route",
        "status": "success"
    }