# Use python tabula module to convert PDF to csv file
import tabula

tabula.io.convert_into('A_PDF_file.pdf', 'A_CSV_file.csv', output_format='csv', pages='all')