from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter

# Ruta del archivo PDF de la plantilla
template_pdf_path = 'template.pdf'

# Open the PDF file
with open(template_pdf_path, 'rb') as template_file:
    reader = PdfReader(template_file)

    # Get the page content
    page = reader.pages[0]

    page_content = page.extract_text()

    # Replace the text
    new_content = page_content.replace("SUDAMERIS", "PEPE")


c = canvas.Canvas("hello-world.pdf",pagesize=A4)
c.drawString(50,50,new_content)
c.save()

print("Finished")       