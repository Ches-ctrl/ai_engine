from flask import jsonify, request
from http import HTTPStatus
from app.common.types import ApiResponse, ErrorDetail
from app.common.errors import error_logger
from app.routes import bp
from app.jobs import fetch_jobs
import uuid

@bp.route('/abc_route', methods=['GET'])
def api_endpoint():
    try:
        # Call fetch_jobs function
        jobs_data = fetch_jobs(title_filter='Consultant')
        
        response = ApiResponse(
            success=True,
            data={'jobs': jobs_data}
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
