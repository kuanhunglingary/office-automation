#  Convert xls files to xlsx using python pandas module
import pandas as pd
import os

df = pd.read_excel('file1.xls')

df.to_excel('file1.xlsx')