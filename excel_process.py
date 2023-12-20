import os
from datetime import datetime
from docx2pdf import convert
from word_file_generator_tables import replace_text_in_word_file


def delete_docx_file(file_path):
    try:
        # Check if the file exists before attempting to delete
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"The file {file_path} has been deleted.")
        else:
            print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_excel_row(row):

    # Convert the date columns to datetime and format them
    # row['desde'] = datetime.strptime(row['desde'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')
    # row['hasta'] = datetime.strptime(row['hasta'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')

    # Format the date columns
    row['emisión'] = row['emisión'].strftime('%d/%m/%Y')
    row['nacimiento'] = row['nacimiento'].strftime('%d/%m/%Y')
    row['desde'] = row['desde'].strftime('%d/%m/%Y')
    row['hasta'] = row['hasta'].strftime('%d/%m/%Y')

    # Format the numeric columns
    numeric_columns = ['fallecimiento', 'incapacidad','prima', 'impuesto', 'premio', 'financiamiento', 'interés', 'costo', 'final']
    for column in numeric_columns:
        row[column] = '{:,}'.format(row[column]).replace(',', '.')    

    replacements = {'{certificado}': row['certificado'], '{emisión}': row['emisión'], '{póliza}': row['póliza'], 
                    '{contratante}': row['contratante'], '{ruc}': row['ruc'], '{nombre}': row['nombre'], 
                    '{documento}': row['documento'], '{nacimiento}': row['nacimiento'], '{domicilio}': row['domicilio'], '{localidad}': row['localidad'],
                    '{plazo}': row['plazo'], '{amortización}': row['amortización'], '{desde}': row['desde'], '{hasta}': row['hasta'], 
                    '{días}': row['días'], '{fallecimiento}': row['fallecimiento'], '{incapacidad}': row['incapacidad'], 
                    '{prima}': row['prima'], '{impuesto}': row['impuesto'], '{premio}': row['premio'], 
                    '{financiamiento}': row['financiamiento'], '{interés}': row['interés'], '{costo}': row['costo'], 
                    '{final}': row['final']}

    # Form the new file name by concatenating the base name with the value of '{nombre}'
    new_file = f'output/new_file_{row["nombre"]}.docx'

    # Call the function
    replace_text_in_word_file('templates/template_edit.docx', new_file, replacements)

    # Convert the Word document to PDF
    convert(new_file, new_file.replace('.docx', '.pdf'))

    # Delete the Word document
    delete_docx_file(new_file)