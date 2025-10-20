import matplotlib.pyplot as plt
sub = ["AI", "Data Science", "Networking", "Cybersecurity"]
counts = [40, 35, 15, 10]
plt.pie(counts, labels=sub, autopct='%1.1f%%')
plt.title("Distribution of MCA Students' Specializations")
plt.show()