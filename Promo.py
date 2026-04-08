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

df = pd.merge(all_files[0], all_files[1], how='right', on='product_id')
pd.set_option('display.max_columns', None)


df = df[df['level1'] == 'Сыры']
df['is_promo'] = df['regular_price'] > df['price']

promo = df[df['is_promo'] == True]['quantity'].sum() / df['quantity'].sum()

non_promo = df[df['is_promo'] == False]['quantity'].sum() / df['quantity'].sum()

sizes = [promo, non_promo]
labels = ['Промо', 'Без промо']

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title('Доля промо-продаж в категории "Сыры"')
plt.tight_layout()
plt.show()

