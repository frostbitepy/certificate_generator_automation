import pandas as pd
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# Leer el archivo Excel
df = pd.read_excel('operaciones.xls')

# Ruta de tu plantilla PDF
plantilla_pdf = 'template.pdf'

# Iterar sobre las filas del DataFrame
for index, row in df.iterrows():
    # Obtener los valores de cada columna
    nombre = row['NOMBRE']
    ci_n = row['C.I.N']
    fecha_nac = row['FECHA NAC.']
    # ... (obtén los valores de las demás columnas)

    # Generar el nombre del archivo PDF de salida
    nombre_archivo_pdf = f'output/{nombre}_{ci_n}_modificado.pdf'

    # Crear un objeto PdfFileWriter para modificar el PDF
    pdf_writer = PdfWriter()

    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
        # Obtener los valores de cada columna
        nombre = row['NOMBRE']
        ci_n = row['C.I.N']
        fecha_nac = row['FECHA NAC.']
        # ... (obtener los valores de las demás columnas)

        # Generar el nombre del archivo PDF de salida
        nombre_archivo_pdf = f'{nombre}_{ci_n}_modificado.pdf'

        # Crear un objeto PdfFileWriter para el nuevo PDF
        pdf_writer = PdfWriter()

        # Abrir el archivo PDF de la plantilla
        with open(plantilla_pdf, 'rb') as plantilla:
            # Crear un objeto PdfFileReader para leer la plantilla
            pdf_reader = PdfReader(plantilla)

            # Agregar todas las páginas de la plantilla al objeto PdfFileWriter
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader._get_page(page_num)
                pdf_writer.add_page(page)

                # Aquí puedes agregar código para modificar el contenido de las páginas
                # Por ejemplo, agregar texto en posiciones específicas

                # Agregar texto modificado
                page.mergePage()
                pdf_writer._get_page(page_num).drawString(100, 750, f'Nombre: {nombre}')
                pdf_writer._get_page(page_num).drawString(100, 730, f'C.I.N: {ci_n}')
                pdf_writer._get_page(page_num).drawString(100, 710, f'Fecha Nac.: {fecha_nac}')
                # ... (agregar texto modificado para las demás columnas)

        # Guardar el archivo PDF modificado
        with open(nombre_archivo_pdf, 'wb') as pdf_salida:
            pdf_writer.write(pdf_salida)

    # Imprimir un mensaje cuando se haya completado la generación de PDFs
    print("Se han generado los archivos PDF modificados.")