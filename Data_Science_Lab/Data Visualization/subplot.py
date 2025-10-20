import matplotlib.pyplot as plt
student_names = ["Asha", "Ravi", "Neha", "Rahul", "Meera"]
marks = [78, 85, 67, 90, 72]
plt.subplot(1, 2, 1)
plt.plot(student_names, marks)
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Marks Obtained by MCA Students")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temp = [24, 26, 29, 32, 34, 30]
plt.subplot(1, 2, 2)
plt.scatter(months, temp)
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.title("Monthly Average Temperature")
plt.tight_layout()
plt.show()