# Create a DataFrame from a Dictionary
"""
Convert the below dictionary to data frame
data = {
         'Name': ['Asha', 'Ravi', 'Neha', 'Rahul', 'Meera'],
         'Age': [22, 23, 21, 24, 22],
         'Marks': [85, 78, 92, 88, 76]
       }
"""

import pandas as pd
data = {
         'Name': ['Asha', 'Ravi', 'Neha', 'Rahul', 'Meera'],
         'Age': [22, 23, 21, 24, 22],
         'Marks': [85, 78, 92, 88, 76]
       }
df = pd.DataFrame(data)
print(df)