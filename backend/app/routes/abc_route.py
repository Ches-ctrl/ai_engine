from flask import Blueprint, jsonify

bp = Blueprint('abc', __name__)

@bp.route('/abc', methods=['GET'])
def abc():
    return jsonify({"message": "ABC route"})
