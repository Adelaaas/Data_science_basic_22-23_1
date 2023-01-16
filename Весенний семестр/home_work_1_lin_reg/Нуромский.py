import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("garments_worker_productivity.csv")

# В датафрейме имеются пропуски
df.isna().sum()

# Пожертвуем пятью строками чтобы всё было хорошо
df = df.dropna()

for i in range(df.iloc[:, 0].size):
    date = df.iloc[i, 0].split("/")
    st = date[2]
    if int(date[1]) < 10:
        st += "0"
    st += date[1]
    if int(date[0]) < 10:
        st += "0"
    st += date[0]
    df.iloc[i, 0] = int(st)

for i in range(df.iloc[:, 1].size):
    df.iloc[i, 1] = int(df.iloc[i, 1].replace("Quarter", ""))

for i in range(df.iloc[:, 3].size):
    df.iloc[i, 3] = df.iloc[i, 3].replace("Monday", "1")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Tuesday", "2")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Wednesday", "3")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Thursday", "4")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Saturday", "6")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Sunday", "7")
    df.iloc[i, 3] = int(df.iloc[i, 3])

# Посмотрим корреляции
plt.figure(figsize=(12,10), dpi= 80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.show()

y = df.iloc[:, 14]
x = pd.concat([df.iloc[:, 0:1], df.iloc[:, 3:14]], axis=1)
X_train, X_test, y_train, y_test = train_test_split(x, y)

# Создание модели регрессии
reg = LinearRegression()
reg.fit(X_train, y_train)

# Коэффиценты модели
print("Коэффиценты:", reg.intercept_, reg.coef_)

# Уравнение
print("Уравнение: y =", reg.intercept_, " ".join(["+ " + str(reg.coef_[i]) + "x" + str(i) for i in range(reg.coef_.size)])
)

# Предсказание
y_pred = reg.predict(X_test)

# Вывод
print(mean_absolute_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

y = df.iloc[:, 14] 
x = pd.concat([df.iloc[:, 0:1], df.iloc[:, 3:14]], axis=1) 
x = x[["targeted_productivity"]] 
X_train, X_test, y_train, y_test = train_test_split(x, y)

y_pred = reg.predict(X_test) 

# График

plt.scatter(X_test['targeted_productivity'],y_test)
plt.scatter(X_test['targeted_productivity'],y_pred)
plt.show()
