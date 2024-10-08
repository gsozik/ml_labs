import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

train = pd.read_csv('Billionaires.csv')

del train['latitude_country']
del train['longitude_country']

'''
Скачать один из наборов данных
Загрузить данные в датафрейм
Вывести статистическую информацию о наборе данных
Вывести названия столбцов и строк
Заменить категориальные данные количественными
Визуализировать данные с помощью Matplotlib и Seaborn
Должно быть не менее 2х визуализаций на каждый признак. Выберите самые красивые визуализации!
Должно быть не менее 3х групповых визуализаций
'''
train = train.dropna()

print(f'{train.head()}\n\n\n')
print(f'{train.describe(include=['O'])}\n\n\n')
print(f'{train.info()}\n\n\n')

plt.figure(figsize=(10,6))
sns.histplot(train['age'])
plt.title('Distribution of Final Worth')
plt.xlabel('age')
plt.ylabel('Frequency')
plt.show()
