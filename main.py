import pandas as pd
from excel_process import process_excel_row

# Read the Excel file
df = pd.read_excel('operaciones_copia.xls')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Call the function
    process_excel_row(row)

print("Finished")