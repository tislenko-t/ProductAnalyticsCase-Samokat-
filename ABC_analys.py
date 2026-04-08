import os

import numpy as np
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

df = pd.merge(all_files[0], all_files[1], how='inner', on='product_id')
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.6f}'.format)

df['revenue'] = df['quantity']*df['price']
df = df.groupby('level2').agg({'revenue': 'sum', 'quantity': 'sum'}).reset_index()

df = df.sort_values(by=['revenue', 'level2'], ascending=False)
df['revenue_contrib'] = df['revenue'] / sum(df['revenue'])
df['revenue_cum'] = df['revenue_contrib'].cumsum()
df['abc_revenue'] = np.where(df['revenue_cum']< 0.8, 'A',
                                   np.where(df['revenue_cum']< 0.95, 'B','C'))


df = df.sort_values(by=['quantity', 'level2'], ascending=False)
df['col'] = df['quantity']/ sum(df['quantity'])
df['cum_col'] = df['col'].cumsum()
df['abc_col'] = np.where(df['cum_col']< 0.8, 'A',
                                   np.where(df['cum_col']< 0.95, 'B','C'))


df['abc'] = df['abc_col'] + ' ' + df['abc_revenue']

print(df)
