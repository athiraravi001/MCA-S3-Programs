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

# -----------------------------------------------------------------------------------------------------------------
# Write a Python program to create a DataFrame with missing values and show how to remove rows and columns containing missing values using dropna().

"""
import pandas as pd
import numpy as np
df = pd.DataFrame({
                   'A': [1, 2, np.nan, 4],
                   'B': [np.nan, 2, 3, 4]
                 })
print("Original DataFrame:\n", df)

df_rows = df.dropna()
print("\nAfter Dropping Rows with Missing Values:\n", df_rows)

df_cols = df.dropna(axis=1)
print("\nAfter Dropping Columns with Missing Values:\n", df_cols)
"""
