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