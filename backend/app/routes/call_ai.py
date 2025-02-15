from flask import request, jsonify
from http import HTTPStatus
from app.routes import bp
from app.common.types import ApiResponse, ErrorDetail
from app.common.errors import error_logger
from app.get_ai import send_info_to_agent, send_info_to_asian
import uuid

@bp.route('/call_ai', methods=['GET'])
def call_ai():
    try:
        result = send_info_to_agent()
        response = ApiResponse(
            success=True,
            data=result
        )
        
        return jsonify(response.model_dump()), HTTPStatus.OK  # Convert to JSON response
    
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
