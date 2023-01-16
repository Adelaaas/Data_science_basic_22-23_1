import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("garments_worker_productivity.csv")

# Посмотрим корреляции
plt.figure(figsize=(12,10), dpi= 80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.show()

# Найдём самый предсказуемый параметр
abs(df.corr()).sum()
# будем предсказывать smv

# Пожертвуем пятью строками чтобы всё было хорошо
df = df.dropna()

y = df.iloc[:, 6]
x = pd.concat([df.iloc[:, 1], df.iloc[:, 4:6], df.iloc[:, 7:15]], axis=1)

for i in range(x.iloc[:, 0].size):
    x.iloc[i, 0] = x.iloc[i, 0].replace("Quarter", "")

# Создание модели регрессии
reg = LinearRegression()
reg.fit(x, y)

# Коэффиценты модели
print("Коэффиценты:", reg.intercept_, reg.coef_)

# Уравнение
print("Уравнение: y =", reg.intercept_, " ".join(["+ " + str(reg.coef_[i]) + "x" + str(i) for i in range(reg.coef_.size)])
)

# Предсказание
y_pred = reg.predict(x)

# Вывод
mean_absolute_error(y, y_pred)
mean_squared_error(y, y_pred)
r2_score(y, y_pred)

# Получились посредственные результаты. Возможно, для получения лучших результатов, стоило бы не откидывать нечисловые данные, а преобразовать их в числовые
