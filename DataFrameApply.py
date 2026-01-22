import pandas as pd

df = pd.read_csv('8-apply_function_data.csv')
# def salary_category(salary):
#     if salary < 50000:
#         return 'Low'
#     elif 50000 <= salary < 100000:
#         return 'Medium'
#     else:
#         return 'High'
# df['Salary_Category'] = df['Salary'].apply(salary_category)

# def experience_performance(performance, experience):
#     if experience > 10:
#         return performance + 1
#     else:
#         return performance
    
# df['Exp_Performance_Score'] = df.apply(lambda i: experience_performance(i['Performance_Score'], i['Experience']), axis=1)

# def adjust_new(row):
#     if row['Experience'] > 10:
#         return row['Performance_Score'] + 1
#     else:
#         return row['Performance_Score']
    
# df['Adjusted_Performance'] = df.apply(adjust_new, axis=1)

# df['Formatted_Name'] = df['Name'].apply(lambda x : x.replace('_', ' '))
# df = df.sort_values(by='Department', ascending=False).reset_index(drop=True)

print(df.head(20))