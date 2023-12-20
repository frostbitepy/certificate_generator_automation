from flask import Flask, send_file
import pandas as pd
from excel_process import process_excel_row

app = Flask(__name__)

# Read the Excel file
df = pd.read_excel('operaciones_copia.xls')

@app.route('/descargar_pdf/<nombre>')
def descargar_pdf(nombre):
    # Find the row with the given name
    row = df[df['nombre'] == nombre].iloc[0]

    # Generate the PDF
    pdf_file = process_excel_row(row)  # This function should return the path of the generated PDF

    # Send the PDF file
    return send_file(pdf_file, mimetype='application/pdf', as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)