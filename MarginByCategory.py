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

df['revenue'] = df['price'] * df['quantity']
df['m'] = (df['price'] - df['cost_price'])*df['quantity']

df_grouped = df.groupby('level1').agg({
    'm': 'sum',
    'revenue': 'sum'
}).reset_index()
df_grouped['perc'] = (df_grouped['m'] / df_grouped['revenue'] * 100)

df_sort_m = df_grouped.sort_values('m', ascending=True)

df_sort_perc = df_grouped.sort_values('perc', ascending=True)


fig, ax = plt.subplots(figsize=(15, 9))

ax.barh(df_sort_m['level1'], df_sort_m['m'])

for i, v in enumerate(df_sort_m['m']):
    ax.text(v + 10, i, f'{v:,.0f}', va='center')

ax.set_title('Маржа по категориям (руб.)')
ax.set_xlabel('Маржа')
ax.set_ylabel('Категория')
ax.tick_params(axis='y', labelsize=9)

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(15, 9))

ax.barh(df_sort_perc['level1'], df_sort_perc['perc'])

for i, v in enumerate(df_sort_perc['perc']):
    ax.text(v+0.1, i, f'{v:.1f}%', va='center')

ax.set_title('Маржинальность по категориям (%)')
ax.set_xlabel('Процент')
ax.set_ylabel('Категория')
ax.tick_params(axis='y', labelsize=9)

plt.tight_layout()
plt.show()
