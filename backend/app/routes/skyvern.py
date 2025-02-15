from flask import Blueprint, request, jsonify
import os
import requests
from http import HTTPStatus

skyvern_routes = Blueprint('skyvern', __name__)

SKYVERN_API_KEY = os.getenv('SKYVERN_API_KEY')
SKYVERN_BASE_URL = 'https://api.skyvern.com/api/v1'

@skyvern_routes.route('/apply', methods=['POST'])
def submit_job_application():
    try:
        data = request.get_json()

        # Validate required fields
        if not data:
            return jsonify({"error": "No data provided"}), HTTPStatus.BAD_REQUEST

        workflow_id = data.get('workflow_id', 'wpid_360548693536008528')

        # Prepare the request to Skyvern
        headers = {
            "Content-Type": "application/json",
            "x-api-key": SKYVERN_API_KEY
        }

        payload = {
            "data": data.get('application_data', {}),
            "proxy_location": "RESIDENTIAL"
        }

        # Send request to Skyvern
        response = requests.post(
            f"{SKYVERN_BASE_URL}/workflows/{workflow_id}/run",
            headers=headers,
            json=payload
        )

        response.raise_for_status()
        return jsonify(response.json()), HTTPStatus.OK

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_GATEWAY
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@skyvern_routes.route('/tasks/<task_id>/steps', methods=['GET'])
def get_task_steps(task_id):
    try:
        # Get pagination parameters with defaults
        page = request.args.get('page', 1, type=int)
        page_size = request.args.get('page_size', 15, type=int)

        headers = {
            "Content-Type": "application/json",
            "x-api-key": SKYVERN_API_KEY
        }

        # Fetch task steps from Skyvern
        response = requests.get(
            f"{SKYVERN_BASE_URL}/tasks/{task_id}/steps",
            headers=headers,
            params={'page': page, 'page_size': page_size}
        )

        response.raise_for_status()
        return jsonify(response.json()), HTTPStatus.OK

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_GATEWAY
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@skyvern_routes.route('/tasks/<task_id>/steps/<step_id>/artifacts', methods=['GET'])
def get_step_artifacts(task_id, step_id):
    try:
        headers = {
            "Content-Type": "application/json",
            "x-api-key": SKYVERN_API_KEY
        }

        # Fetch artifacts for the specific step
        response = requests.get(
            f"{SKYVERN_BASE_URL}/tasks/{task_id}/steps/{step_id}/artifacts",
            headers=headers
        )

        response.raise_for_status()
        return jsonify(response.json()), HTTPStatus.OK

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_GATEWAY
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@skyvern_routes.route('/tasks/<task_id>/screenshots', methods=['GET'])
def get_task_screenshots(task_id):
    try:
        headers = {
            "Content-Type": "application/json",
            "x-api-key": SKYVERN_API_KEY
        }

        # First get all steps for the task
        steps_response = requests.get(
            f"{SKYVERN_BASE_URL}/tasks/{task_id}/steps",
            headers=headers
        )
        steps_response.raise_for_status()
        steps = steps_response.json()

        # Collect screenshots from each step
        screenshots = []
        for step in steps.get('items', []):
            step_id = step['id']
            artifacts_response = requests.get(
                f"{SKYVERN_BASE_URL}/tasks/{task_id}/steps/{step_id}/artifacts",
                headers=headers
            )
            artifacts_response.raise_for_status()
            artifacts = artifacts_response.json()

            # Filter for screenshot artifacts and add step context
            for artifact in artifacts.get('items', []):
                if artifact['type'] == 'screenshot':
                    screenshots.append({
                        'step_name': step.get('name'),
                        'step_status': step.get('status'),
                        'timestamp': step.get('created_at'),
                        'screenshot_url': artifact['url'],
                        'step_id': step_id
                    })

        return jsonify({
            'screenshots': screenshots,
            'total': len(screenshots)
        }), HTTPStatus.OK

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_GATEWAY
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
