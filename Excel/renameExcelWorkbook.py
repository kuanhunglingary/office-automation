#   Rename Workbook Name Using Python openpyxl module
import openpyxl
import os

os.chdir('D:/gary')

excel_file = openpyxl.load_workbook("file1.xlsx")

excel_sheet = excel_file.get_sheet_by_name('Workbook00')

excel_sheet.title = 'Workbook01'

excel_file.save('file1.xlsx')