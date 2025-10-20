import matplotlib.pyplot as plt
import numpy as np
ages = np.random.randint(20, 31, size=100)
plt.hist(ages, bins=5, edgecolor='black')
#plt.hist(ages, bins=10, edgecolor='black')
#plt.hist(ages, bins=20, edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of MCA Student Ages")
plt.show()