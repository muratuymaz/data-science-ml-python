import pandas as pd
import numpy as np

grades = {
    "Atil":50,
    "Buse":60,
    "Cem":70,
}
# grades_series = pd.Series(grades)
# print(grades_series)
names = ["Atil","Buse","Cem"]
grades_list = [50,60,70]
grades_series = pd.Series(data=grades_list, index=names)
# print(grades_series)
numpy_grades = np.array([50,60,70])
# print(pd.Series(numpy_grades))

contest_results = pd.Series(data=[1,2,3,4,5],index=["Atil","Buse","Cem","Derya","Efe"])
contest_results2 = pd.Series(data=[20,50,10,40,80],index=["Atil","Murat","Merve","Derya","Efe"])

# print(contest_results + contest_results2)
# key-value eşleşmesi yapar ve ona gore datalari toplar,olmayanlara NaN verir

data = np.array([[50,60,70],[80,90,100],[40,60,80],[70,80,90]])
df = pd.DataFrame(data, index=["Atil","Buse","Cem","Derya"], columns=["Math","Physics","Chemistry"])
# print(df)

# DataFrame cok boyutlu dizilerle calismak icin kullanilir
# Series tek boyutlu dizilerle kullanilir bu yuzden daha cok dataframe kullanilir
# DataFrame serieslerin bir araya gelmesiyle olusur

# mean = df["Math"].mean()
# x = df["Math"].std()
# print("Math ortalamasi:", mean)
# print("Math standart sapmasi:", x)

# new_df = df[["Math","Chemistry"]]
# print(new_df)
# new_df = df.loc[["Atil"]]
# print(new_df)
# new_df = df.iloc[0:2,1:3]
# new_df = df
# new_df["Biology"] = [60,70,80,90]
# print(new_df)
# new_df.drop("Physics", axis=1, inplace=True)
# print(new_df)

new_df = df
# print(new_df)
# new_df = df.reset_index()
print(new_df)
print(new_df.loc["Atil"])
