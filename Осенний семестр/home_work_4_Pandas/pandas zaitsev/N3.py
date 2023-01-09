import pandas as pd

x_train = pd.read_csv('https://raw.githubusercontent.com/Adelaaas/Data_science_basic_22-23_1/main/class_work_4_Pandas/ONTI%20Students%20performance/X_train.csv')
y_train = pd.read_csv('https://raw.githubusercontent.com/Adelaaas/Data_science_basic_22-23_1/main/class_work_4_Pandas/ONTI%20Students%20performance/y_train.csv')

f_df = pd.concat([x_train, y_train], axis=0, ignore_index=True)

na = f_df.isna().sum()