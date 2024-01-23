# Combine multiple  Excel files using python pandas module
from operator import index
import pandas as pd
import datetime as dt

files = ['1_data.xlsx','2_data.xlsx','3_data.xlsx','4_data.xlsx','5_data.xlsx','6_data.xlsx','7_data.xlsx','8_data.xlsx']

combined = pd.DataFrame()

for file in files:
    df=pd.read_excel(file)
    combined=combined.append(df,ignore_index=True)

combined.to_excel('combine.xlsx',index=False,sheet_name='data')