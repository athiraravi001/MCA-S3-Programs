import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
         "Name": ["Asha", "Arun", "Binu", "Devi", "Anu", "Jithu"],
         "Department": ["CSE", "ECE", "CSE", "EEE", "CSE", "ECE"]
       }
df = pd.DataFrame(data)
sns.countplot(x="Department", data=df, hue="Department")
plt.xlabel('Department')
plt.ylabel('Name')
plt.show()
# p = sns.countplot(x="Department", data=df, hue="Name")
# p.set_xlabel('Department')
# p.set_ylabel('Name')
