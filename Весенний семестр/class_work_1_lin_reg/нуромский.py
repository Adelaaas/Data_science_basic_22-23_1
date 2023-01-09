import numpy as np
import pandas as pd


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.datasets import load_boston

boston = load_boston()
columns = ['target'] + list(boston.feature_names)
df = pd.DataFrame(data=np.c_[boston.target, boston.data], columns=columns)

y = df.iloc[:, 0]
x = df.iloc[:, 1:]

# Создание модели регрессии
reg = LinearRegression()
reg.fit(x, y)

# Коэффиценты модели
print(reg.intercept_, reg.coef_)

# Уравнение
print("y =", reg.intercept_, " ".join(["+ " + str(reg.coef_[i]) + "x" + str(i) for i in range(reg.coef_.size)])
)

# Предсказание
y_pred = reg.predict(x)