import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pybit




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


train_category = train['category'].value_counts().head(10).plot(kind = 'bar',fontsize = 7)

plt.figure(figsize=(10,6))
sns.scatterplot(x='age', y='finalWorth', data=train)
plt.title('Age vs Final Worth')
plt.xlabel('Age')
plt.ylabel('Final Worth (in millions)')
plt.show()

train["finalWorth_group"] = pd.cut(x=train['finalWorth'], bins=[0, 2500, 5000, 7500, 10000, 15000, 30000, 60000, 100000, 150000, 200000])
plt.title('The number of men and women millionaires')
plt.xticks(rotation=45, fontsize = 7)
sns.countplot(data=train, hue = 'gender', x='finalWorth_group')
plt.show()

