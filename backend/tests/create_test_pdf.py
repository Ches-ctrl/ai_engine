from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_sample_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.drawString(100, 750, "Sample CV")
    c.drawString(100, 700, "Name: John Doe")
    c.drawString(100, 650, "Email: john@example.com")
    c.drawString(100, 600, "Skills: Python, Flask, Web Development")
    c.save()

if __name__ == '__main__':
    create_sample_pdf('tests/fixtures/sample_cv.pdf')
