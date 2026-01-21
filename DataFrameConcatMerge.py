import numpy as np
import pandas as pd

# concat
df1 = pd.read_csv('7-concat_data1.csv')
df2 = pd.read_csv('7-concat_data2.csv')
df = pd.concat([df1, df2],ignore_index=True)

# merge
dfMerge1 = pd.read_csv('7-merge_data1.csv')
dfMerge2 = pd.read_csv('7-merge_data2.csv')

# merge outer join : iki dataframe deki tum verileri alir
df = pd.merge(dfMerge1, dfMerge2, on=['Employee_ID'], how='outer')

# merge left join : sol dataframe deki tum verileri alir, sagdaki ile eslesenleri ekler
df = pd.merge(dfMerge1, dfMerge2, on=['Employee_ID'], how='left')

# merge right join : sag dataframe deki tum verileri alir, soldaki ile eslesenleri ekler
df = pd.merge(dfMerge1, dfMerge2, on=['Employee_ID'], how='right')

# merge inner join : sadece iki dataframe deki eslesen verileri alir
df = pd.merge(dfMerge1, dfMerge2, on=['Employee_ID'], how='inner')

print(df)