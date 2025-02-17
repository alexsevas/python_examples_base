# pip install seaborn

import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd

# Пример данных
data = pd.DataFrame({
    'price': [200000, 150000, 300000, 350000, 500000],
    'area': [70, 50, 100, 120, 200]
})

# Построение графика
sns.scatterplot(x='area', y='price', data=data)
plt.title('Price vs Area')
plt.show()


# с помощью hue можно добавить третий фактор, например, категориальный
data['type'] = ['apartment', 'apartment', 'house', 'house', 'villa']

sns.scatterplot(x='area', y='price', hue='type', data=data)
plt.title('Price vs Area with Property Types')
plt.show()


# Пример плотности и гистограммы
sns.histplot(data=data, x='price', kde=True)
plt.title('Price Distribution')
plt.show()