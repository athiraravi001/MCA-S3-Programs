# Write a program that populates an array with numbers that lie in the range of 0 – 50 and are also divisible by 5. Use the List Comprehension method.

import numpy as np
ar = np.array([x for x in range(0,51) if x%5==0])
print(ar)