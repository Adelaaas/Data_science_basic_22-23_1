import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("garments_worker_productivity.csv")

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
    df.iloc[i, 0] = st

for i in range(df.iloc[:, 1].size):
    df.iloc[i, 1] = df.iloc[i, 1].replace("Quarter", "")

for i in range(df.iloc[:, 3].size):
    df.iloc[i, 3] = df.iloc[i, 3].replace("Monday", "1")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Tuesday", "2")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Wednesday", "3")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Thursday", "4")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Saturday", "6")
    df.iloc[i, 3] = df.iloc[i, 3].replace("Sunday", "7")

y = df.iloc[:, 14]
x = pd.concat([df.iloc[:, 0:2], df.iloc[:, 3:14]], axis=1)

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

# Получились довольно неплохие данные
