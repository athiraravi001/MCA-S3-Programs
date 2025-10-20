import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Step 1: Create a simple DataFrame
data = {
         "Math":    [85, 78, 92, 88, 76],
         "Science": [80, 75, 89, 90, 70]
       }
students = ["Asha", "Ravi", "Neha", "Rahul", "Meera"]
d = pd.DataFrame(data, index=students)
print(d)
# Step 2: Plot heatmap on students mark
plt.figure(figsize=(6,4))
sns.heatmap(d, annot=True, cmap="Greens")
#sns.heatmap(d, annot=True)
plt.show()