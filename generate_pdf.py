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

    # Initialize a new writer
    writer = PdfWriter()

    # Crear una nueva página con el contenido modificado
    new_page = writer.add_blank_page(width=8.27 * 72, height=11.7 * 72)

    # Copiar el contenido de la página original
    new_page.merge_page(page)

    # Sobrescribir el método extract_text
    new_page.extract_text = lambda: new_content

# Guardar el archivo PDF modificado
with open("modified.pdf", "wb") as modified_file:
    writer.write(modified_file)

print("Finished")