import pandas as pd
from pptx import Presentation

excel_file = "data.xlsx"
df = pd.read_excel(excel_file, engine='openpyxl')

print(df)
