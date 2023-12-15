from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_pdf(output_pdf_path):
    # Create a PDF canvas
    pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=letter)

    # Set the font and font size
    pdf_canvas.setFont("Helvetica", 12)

    # Define the number of rows and columns in the grid
    rows = 4
    columns = 2

    # Set the width and height of the cells
    cell_width = letter[0] / columns
    cell_height = letter[1] / rows

    # Draw the grid
    for row in range(rows):
        for col in range(columns):
            x = col * cell_width
            y = letter[1] - (row + 1) * cell_height

            # Draw a rectangle for each cell
            pdf_canvas.rect(x, y, cell_width, cell_height)

            # Optional: Add text to each cell
            cell_text = f"Cell {row + 1}-{col + 1}"
            pdf_canvas.drawString(x + 5, y + cell_height - 15, cell_text)

    # Save the canvas to the PDF file
    pdf_canvas.save()

if __name__ == "__main__":
    output_path = 'grid_reportlab.pdf'
    generate_pdf(output_path)