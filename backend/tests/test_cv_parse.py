import requests
import os

def test_cv_parse():
    # URL of your Flask application
    url = 'http://localhost:5000/parse-cv'

    # Path to a test PDF file
    pdf_path = 'tests/fixtures/sample_cv.pdf'

    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create the files dictionary
        files = {
            'file': ('cv.pdf', pdf_file, 'application/pdf')
        }

        # Make the POST request
        response = requests.post(url, files=files)

        # Print the response
        print(response.json())

        # Basic assertions
        assert response.status_code == 200
        assert 'text' in response.json()
        assert 'status' in response.json()
        assert response.json()['status'] == 'success'

if __name__ == '__main__':
    test_cv_parse()
