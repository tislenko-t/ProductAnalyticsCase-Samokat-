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

product_groups = (df.groupby(['level1'])['quantity'].sum().reset_index().sort_values(
    by=['quantity'], ascending=False))
top_10 = product_groups.head(5)


plt.figure(figsize=(16, 8))

categories = product_groups['level1'].unique()
colors = sns.color_palette("viridis", len(categories))

sns.barplot(data=product_groups, x='level1', y='quantity', dodge=False)

plt.title('Самые ходовые товарные группы', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Наименование товара',  fontsize=14, fontweight='bold')
plt.ylabel('Количество проданных единиц (шт.)', fontsize=14, fontweight='bold')
plt.xticks(rotation=30, ha='right', fontsize=11)

print(product_groups.head(5))

plt.tight_layout()
plt.show()
