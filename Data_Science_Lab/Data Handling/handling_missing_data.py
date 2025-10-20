"""
Create sample data with missing values
data = {
         'Name': ['Asha', 'Ravi', 'Neha', 'Rahul', 'Meera'],
         'Marks': [85, None, 92, None, 76]
       }

Fill missing values with average
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
print(df)
"""

import pandas as pd
data = {
         'Name': ['Asha', 'Ravi', 'Neha', 'Rahul', 'Meera'],
         'Marks': [85, None, 92, None, 76]
       }
df = pd.DataFrame(data)
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())      # Fill missing values in 'Marks' column with the average
print(df)