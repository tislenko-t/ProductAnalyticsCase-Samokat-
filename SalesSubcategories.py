import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

folder = 'data'
all_files =[]
for file in os.listdir(folder):
    if file.endswith(".xlsx"):
        file_path = os.path.join(folder, file)
        df = pd.read_excel(file_path, index_col = 0)
        all_files.append(df)

df = pd.merge(all_files[0], all_files[1], how='right', on='product_id')
pd.set_option('display.max_columns', None)
df_sale = df.groupby(['level1', 'level2'])['quantity'].sum().reset_index()
df_sale_sorted = df_sale.sort_values('quantity', ascending=False)
print(df_sale_sorted.head(5))