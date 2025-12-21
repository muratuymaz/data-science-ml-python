import numpy as np
import pandas as pd

data = np.random.randn(4, 3)

# print("NumPy Array:")
# print(data)

# Dataframe cok boyutlu dizilerle (multidimensional arrays) calismak icin kullanilir.
# Series tek boyutlu dizilerle (one-dimensional arrays) calismak icin kullanilir.

dataframe = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3']
                        ,index=['Row1', 'Row2', 'Row3', 'Row4'])

# print("Pandas DataFrame:")
# print(dataframe)

# DataFrame'in belirli bir kolonu nasil secilir?
# column1 = dataframe['Column1']
# print("\nSelected Column (Column1):")
# print(column1)

# DataFrame'in belirli bir satiri nasil secilir?
# row2 = dataframe.loc['Row2']
# print("\nSelected Row (Row2):")
# print(row2)
# DataFrame'in belirli bir satiri index numarasina gore nasil secilir?
# row3 = dataframe.iloc[2]
# print("\nSelected Row (Row3) using iloc:")
# print(row3)
# DataFrame'in belirli bir kolonu index numarasina gore nasil secilir?
# row4 = dataframe.iloc[:,2]
# print("\nSelected Column (Column3) using iloc:")
# print(row4)

# DataFrame'e yeni bir kolon nasil eklenir?
dataframe["Column4"] = np.random.randn(4)
# print(dataframe)

# DataFrame'den bir kolon nasil silinir?
dataframe.drop("Column4", axis=1, inplace=True)
print(dataframe)

