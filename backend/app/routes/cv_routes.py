from flask import Blueprint, request, jsonify, render_template
from flask_cors import cross_origin
import PyPDF2
import io
from ..agent import JobMatchingAgent
import asyncio
import json
import os

# Create the blueprint instance
bp = Blueprint('cv', __name__)
agent = JobMatchingAgent()

def get_jobs():
    """Get jobs from JSON files in data directory"""
    jobs = []
    jobs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'jobs_json')
    for filename in os.listdir(jobs_dir):
        if filename.endswith('.json'):
            with open(os.path.join(jobs_dir, filename)) as f:
                jobs.extend(json.load(f))
    return jobs

# @bp.route('/upload', methods=['GET'])
# def upload_page():
#     return render_template('test_upload.html')

@bp.route('/parse-cv', methods=['POST'])
@cross_origin()
def parse_cv():
    if 'cv' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['cv']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are supported'}), 400

    try:
        # Read the PDF file
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))

        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Process CV and match with jobs
        cv_data = asyncio.run(agent.process_cv(text))
        jobs = get_jobs()  # Get available jobs
        matches = asyncio.run(agent.match_cv_to_jobs(cv_data, jobs))

        return jsonify({
            'cv_data': cv_data,
            'matches': matches,
            'filename': file.filename
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
