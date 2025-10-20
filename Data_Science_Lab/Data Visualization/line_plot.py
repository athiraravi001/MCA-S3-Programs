import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temp = [24, 26, 29, 32, 34, 30]
plt.plot(months, temp)
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.title("Monthly Average Temperature")
plt.show()