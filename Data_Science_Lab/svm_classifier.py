# Import the necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the Iris dataset
iris = datasets.load_iris()
x = iris.data[:, :4] # All four features
y = iris.target

# Split the data into training and testing sets (80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# SVM with Linear Kernel
svm_linear = SVC(kernel="linear", gamma=0.3, C=10)
svm_linear.fit(x_train, y_train)
y_pred_linear = svm_linear.predict(x_test)

print("\n===== Linear Kernel =====")
print("Accuracy:", accuracy_score(y_test, y_pred_linear))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_linear))
print("Classification Report:\n", classification_report(y_test, y_pred_linear))

# SVM with RBF Kernel
svm_rbf = SVC(kernel="rbf", gamma=0.3, C=10)
svm_rbf.fit(x_train, y_train)
y_pred_rbf = svm_rbf.predict(x_test)

print("\n===== RBF Kernel =====")
print("Accuracy:", accuracy_score(y_test, y_pred_rbf))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rbf))
print("Classification Report:\n", classification_report(y_test, y_pred_rbf))

# SVM with Polynomial Kernel
svm_poly = SVC(kernel="poly", degree=3, gamma=0.3, C=10)
svm_poly.fit(x_train, y_train)
y_pred_poly = svm_poly.predict(x_test)

print("\n===== Polynomial Kernel =====")
print("Accuracy:", accuracy_score(y_test, y_pred_poly))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_poly))
print("Classification Report:\n", classification_report(y_test, y_pred_poly))