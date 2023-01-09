import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram, linkage

# pFLFYBT 1
df = pd.read_csv("Credit Card Dataset.csv")

df.isna().sum()
## Отбросим пропуски
df = df.dropna()

## Применим boxplot
sns.boxplot(df['BALANCE'], width=0.3, orient="h")
plt.show()
## Он ничего не показал

## Применим кореллограмму
plt.figure(dpi=80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.show()
## Некоторые корреляции имеются


# KMeans
## Метод локтя
X = df.loc[:,['BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE']]

SSE = []

for k in range(1, 9):
    kmeans = KMeans(n_clusters = k)
    kmeans.fit(X)
    SSE.append(kmeans.inertia_)

plt.plot(range(1,9), SSE, marker='s');
plt.xlabel('k')
plt.ylabel('SSE');
plt.show()
## Наибольший угол при k=2

## Без предсказания
plt.scatter(df['PAYMENTS'],df['PURCHASES'])
plt.xlabel('PAYMENTS')
plt.ylabel('PURCHASES')
plt.show()

## С предсказанием
kmeans = KMeans(n_clusters = 2)
kmeans.fit(X)
Y_pred = kmeans.labels_
plt.plot(X[Y_pred==1]['PAYMENTS'], X[Y_pred==1]['PURCHASES'], 'go', label='class2')
plt.plot(X[Y_pred==0]['PAYMENTS'], X[Y_pred==0]['PURCHASES'], 'bo', label='class1')
plt.xlabel('PAYMENTS')
plt.ylabel('PURCHASES')
plt.show()

# Иерархический
## Дендрограмма
Z = linkage(X, 'ward')
dendrogram(Z)
plt.show()
## Остановимся на трёх кластерах, но тут не очевидно

## Без предсказания
plt.scatter(df['PAYMENTS'],df['PURCHASES'])
plt.xlabel('PAYMENTS')
plt.ylabel('PURCHASES')
plt.show()

## С предсказанием
label = fcluster(Z, 3, criterion='distance')
plt.plot(X[label==1]['PAYMENTS'], X[label==1]['PURCHASES'], 'ro', label='class1')
plt.plot(X[label==2]['PAYMENTS'], X[label==2]['PURCHASES'], 'go', label='class2')
plt.plot(X[label==3]['PAYMENTS'], X[label==3]['PURCHASES'], 'bo', label='class3')
plt.show()
