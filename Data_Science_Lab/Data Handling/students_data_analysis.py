# Read Data from a CSV File

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(".venv/DataSet/Students.csv")
print(df)

# Display first 5 rows and first 3 rows

print("\n========================================\n")
print("First 5 rows : \n", df.head(5))
print("\n========================================\n")
print("First 3 rows : \n", df.head(3))
print("\n========================================\n")

# Select a single column by column name : Name

print("Single column by column name : \n", df['Name'])
print("\n========================================\n")

# Select multiple columns by column name : Name,FinalMark

print("Multiple columns by column name : \n", df[['Name', 'FinalMark']])
print("\n========================================\n")

# Select multiple columns by index (column 1 and column 3)

print("Multiple columns by index (Column 1 and 3):\n", df.iloc[:, [0, 2]])
print("\n========================================\n")

# Select specific row (second row) by index

print("Second row (by index):\n", df.iloc[1])
print("\n========================================\n")

# Add Pass/Fail column based on marks – if FinalMark>40 Pass else Fail

df['Result'] = df['FinalMark'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print(df)
print("\n========================================\n")

# Sort by Marks in descending order

sorted_df = df.sort_values(by='FinalMark', ascending=False)
print(sorted_df)

# Create a count plot  on “Gender”

p=sns.countplot(x='Gender',data=df, hue='Gender')   #hue : different category shows different colors in the graph
p.set_xlabel('Gender')
p.set_ylabel('Student number')
plt.show()