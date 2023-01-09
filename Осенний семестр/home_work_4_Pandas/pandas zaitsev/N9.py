import pandas as pd

studs_info = pd.read_csv('https://raw.githubusercontent.com/Adelaaas/Data_science_basic_22-23_1/main/class_work_4_Pandas/ONTI%20Students%20performance/studs_info.csv')

new_df = studs_info.drop(labels='Статус', axis=1, inplace=True)