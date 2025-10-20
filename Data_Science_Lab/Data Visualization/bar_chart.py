import matplotlib.pyplot as plt
student_names = ["Asha", "Ravi", "Neha", "Rahul", "Meera"]
marks = [78, 85, 67, 90, 72]
plt.bar(student_names, marks)
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Marks Obtained by MCA Students")
plt.show()