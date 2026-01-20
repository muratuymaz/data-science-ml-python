import numpy as np
import pandas as pd

weather_df = pd.read_excel('6-weather.xlsx')

# print(weather_df)

# working with missing data

weather_na_df = pd.read_excel('6-weatherna.xlsx')

# print(weather_na_df)

# print(weather_na_df.isna())

a = weather_na_df.describe()
a = weather_na_df.fillna(0).describe()

df = pd.read_csv('6-employee.csv')
a = df.describe()
a = df.groupby('City')
# a = a['Salary'].mean()
# a = a['Experience'].mean()

print(a)