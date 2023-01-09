import pandas as pd

studs_info = pd.read_csv('https://raw.githubusercontent.com/Adelaaas/Data_science_basic_22-23_1/main/class_work_4_Pandas/ONTI%20Students%20performance/studs_info.csv')

male = studs_info[studs_info['Пол'] == 'М']
df = male[male['Дата выпуска'] == '2019-08-31']
count = df.value_counts()
