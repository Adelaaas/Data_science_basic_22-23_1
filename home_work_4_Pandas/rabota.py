# 1. Посмотреть размерность дата фреймов.
import pandas as pd

print(pd.read_csv("sample_submission.csv").shape)
print(pd.read_csv("studs_info.csv").shape)
print(pd.read_csv("X_test.csv").shape)
print(pd.read_csv("X_train.csv").shape)
print(pd.read_csv("y_train.csv").shape)
print(pd.read_csv("zachety.csv").shape)

# 2. Соедить два датафрейма X_train и y_train в один train по индексам.
import pandas as pd

train = pd.concat([pd.read_csv("X_train.csv"), pd.read_csv("y_train.csv")], axis = 1)
print(train)

# 3. Посчитать пропуски в датафрейме studs_info.
import pandas as pd

pd.isna(pd.read_csv("studs_info.csv")).sum().sum()

# 4. Посчитать сколько уникальных значений в колонке АТТЕСТАЦИЯ и сколько раз каждое из них встречается.
import pandas as pd

print(train['АТТЕСТАЦИЯ'].unique())
print(train['АТТЕСТАЦИЯ'].value_counts())
