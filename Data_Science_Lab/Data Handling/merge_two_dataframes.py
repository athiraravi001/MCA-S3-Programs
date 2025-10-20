import pandas as pd
data1 = {'ID': [1, 2, 3], 'Name': ['Asha', 'Ravi', 'Neha']}
data2 = {'ID': [1, 2, 3], 'Marks': [85, 78, 92]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged = pd.merge(df1, df2, on='ID')
print(merged)