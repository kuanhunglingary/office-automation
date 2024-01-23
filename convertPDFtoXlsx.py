#  Convert PDF file to CSV file
#  Reference : https://www.youtube.com/watch?v=wJwXThPSBE8  (  From 3:48  )
import tabula

tabula.io.convert_into('A_PDF_file.pdf','A_CSV_file.csv', output_format='csv', pages='all')

#  Convert CSV file to xlsx file
#  https://www.youtube.com/watch?v=JFAn-aownHE  (  From 3:45  )

import csv
import openpyxl

csv_data = []

with open('A_CSV_file.csv') as file_obj:
    reader = csv.reader(file_obj)
    for row in reader:
        csv_data.append(row)

wb = openpyxl.Workbook()

sheet = wb.active

for row in csv_data:
    sheet.append(row)

wb.save('A_.xlsx')