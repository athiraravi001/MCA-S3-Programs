# To implement Decision Tree classification using Iris dataset and find the accuracy of the algorithm.

# ===== Import necessary libraries =====
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ======== Load the Dataset ========
iris = datasets.load_iris()           # Load the Iris dataset (features + target labels)
X = iris.data                         # Feature matrix (sepal/petal length & width)
y = iris.target                       # Target labels (0=setosa, 1=versicolor, 2=virginica)

# ======== Split the dataset (70% for training and 30% for testing) ========
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ======== Create and Train Decision Tree Classifier ========
dt_clf = DecisionTreeClassifier(random_state=0)

# Train the classifier on training data
dt_clf.fit(X_train, y_train)

# ======== Make Predictions on Test Data ========
y_pred = dt_clf.predict(X_test)

# ======== Evaluate Model Performance ========
# Print the overall accuracy
print("Accuracy :", accuracy_score(y_test, y_pred))

# Print confusion matrix to see how many instances were correctly/incorrectly classified
print("\nConfusion Matrix :-\n", confusion_matrix(y_test, y_pred))

# Print detailed classification report (precision, recall, f1-score) for each class
print("\nClassification Report :-\n", classification_report(y_test, y_pred))

# ======== Visualize the Decision Tree ========
plt.figure(figsize=(15, 10))  # Set figure size for clarity

# Plot the decision tree
# feature_names -> names of features for readability
# class_names -> class labels for clarity
# filled=True -> fill nodes with colors based on predicted class
plot_tree(dt_clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()
