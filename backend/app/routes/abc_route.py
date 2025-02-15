from flask import jsonify
from http import HTTPStatus
from app.common.types import ApiResponse, ErrorDetail
from app.common.errors import error_logger
from app.routes import bp
import uuid

@bp.route('/abc_route', methods=['GET'])
def api_endpoint():
    try:
        response = ApiResponse(
            success=True,
            data={'data': 'abc_route'}
        )

        return jsonify(response.model_dump()), HTTPStatus.OK
    
    except Exception as error:
        error_id = str(uuid.uuid4())
        error_logger(error, error_id)

        response = ApiResponse(
            success=False,
            error=ErrorDetail(
                code="INTERNAL_ERROR",
                message="An unexpected error occurred",
                error_id=error_id
            )
        )
        return jsonify(response.model_dump()), HTTPStatus.INTERNAL_SERVER_ERROR
