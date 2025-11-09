# Write a program to create a list, tuple, set, and dictionary, then display their values and datatypes.

l = [1, "hello", 3.14, True]      # Create a list
t = (10, "world", False)         # Create a tuple
s = {"apple", "banana", "cherry"}      # Create a set
d = {"name": "Alice", "age": 30, "city": "New York"}       # Create a dictionary

print("--- List ---")
print("Value :", l)
print("Data Type :", type(l))
print("\n")

print("--- Tuple ---")
print("Value:", t)
print("Data Type:", type(t))
print("\n")

print("--- Set ---")
print("Value:", s)
print("Data Type:", type(s))
print("\n")

print("--- Dictionary ---")
print("Value:", d)
print("Data Type:", type(d))

"""
print("List:", l, type(l))
print("Tuple:", t, type(t))
print("Set:", s, type(s))
print("Dictionary:", d, type(d))
"""
print("\n=========================================\n")


# Create a list with 4 elements and do the following in that list
"""
a. Append an item to the list
b. Insert an item with value 40 at the 2 nd position
c. Update the value at the 5 th position
d. Delete item with value 40
e. Delete an item at the 3 rd position
"""

l = [10 ,20, 30, 40]
print("List before modifications : ", l)
l.append(50)
print("List after appending an item : ", l)
l.insert(1, 40)
print("List after inserting an item at the 2nd position : ", l)
l[4] = 100
print("List after updating the value at the 5th position : ", l)
l.remove(40)
print("List after deleting item with value 40 : ", l)
del l[2]
print("List after deleting item at the 3rd position : ", l)
print("\n=========================================\n")


# Create a random list (with 5 members) with values from 1 to 50 and add 10 to each number in random list

import random
random_list = [random.randint(1,50) for _ in range(5)]
print("Random list : ", random_list)
modified_list = [x + 10 for x in random_list]
print("Modified list : ", modified_list)
print("\n=========================================\n")


# Write a program that populates a list by numbers that lies in the range of 0 – 20 and also divisible by 5. Use List Comprehension method.
"""
import numpy as np
l=np.array([x for x in range(0,21) if x%5==0])
print(l)
"""

l = [x for x in range(0, 21) if x % 5 == 0]
print(l)
print("\n=========================================\n")


# Create an empty dictionary

dict = {}
print("Dictionary : ",dict)
print("\n=========================================\n")


# Create a dictionary with mixed keys and integer keys

mixed_keys_dict = {"name" : "Alice", 1 : "New York", "age" : 30}
print("Mixed keys dictionary : ", mixed_keys_dict)
integer_keys_dict = {1 : "apple", 2 : "banana", 3 : "cherry"}
print("Integer keys dictionary : ", integer_keys_dict)


# Convert the array to a list

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array : ",x)
y=x.tolist()
print("List : ",y)
