from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import PyPDF2
import io

# Create the blueprint instance
bp = Blueprint('cv', __name__)

@bp.route('/upload', methods=['GET'])
def upload_page():
    return render_template('test_upload.html')

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

        # Return cleaned up text
        return jsonify({
            'text': text.strip(),
            'filename': file.filename
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
