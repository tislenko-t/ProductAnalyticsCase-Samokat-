import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

folder = 'data'
all_files =[]
for file in os.listdir(folder):
    if file.endswith(".xlsx"):
        file_path = os.path.join(folder, file)
        df = pd.read_excel(file_path)
        all_files.append(df)

df = all_files[1]
pd.set_option('display.max_columns', None)

df_filtered = df[pd.to_datetime(df['accepted_at']).dt.date == pd.to_datetime('2022-01-13').date()]
orders = df_filtered.groupby('order_id').apply(lambda x: (x['price'] * x['quantity']).sum(), include_groups=False).mean().round(3)
print(orders)