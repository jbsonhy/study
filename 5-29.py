from IPython.display import Image

import numpy as np
import pandas as pd
import os

chd = r"e:\coding\Python\Data"

#print(os.path.isdir(chd))
os.chdir(chd)

#print(os.listdir(chd))
excel = pd.read_excel('seoul_transportation.xlsx', sheet_name='철도', engine='openpyxl')
print(excel.head())

excel.to_excel('sample.xlsx', index = True)
excel.to_excel('sample1.xlsx', index=False, sheet_name='샘플')

writer = pd.ExcelWriter('sample2.xlsx')
excel.to_excel(writer, index=False, sheet_name='샘플1')
excel.to_excel(writer, index=False, sheet_name='샘플2')
excel.to_excel(writer, index=False, sheet_name='샘플3')
writer.close()