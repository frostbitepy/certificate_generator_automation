from flask import Flask, send_file
from excel_process import process_excel_row

app = Flask(__name__)

@app.route('/descargar_certificado/<nombre>')
def descargar_certificado(nombre):
    # Genera el certificado
    ruta_certificado = process_excel_row(nombre)  # Esta función debe generar el certificado y devolver la ruta del archivo

    # Envia el archivo
    return send_file(ruta_certificado, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000)