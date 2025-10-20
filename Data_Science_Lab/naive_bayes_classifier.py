# To implement Naïve Bayes Algorithm using any standard dataset available in the public domain (Iris Dataset) and find the accuracy of the algorithm.

# Import required modules
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB  # Gaussian Naive Bayes model
from sklearn.metrics import confusion_matrix  # To evaluate classification performance
from sklearn.metrics import classification_report  # To get detailed performance metrics

# Load Iris dataset and separate features (X) and target labels (Y)
X, Y = load_iris(return_X_y=True)

# Split dataset into training set and testing set (60% for training, 40% for testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=1)
print("\nTraining data shape:", X_train.shape, Y_train.shape)
print("Testing data shape :", X_test.shape, Y_test.shape)

# Create an instance of Gaussian Naive Bayes model
gnb = GaussianNB()

# Train the model using the training data
gnb.fit(X_train, Y_train)

# Predict the class labels for the test set
y_pred = gnb.predict(X_test)

# Print the mean accuracy of the model on the test data
print("\nGaussian Naive bayes score = ", gnb.score(X_test, Y_test))

# Display confusion matrix to see how predictions compare to actual labels
print("\nConfusion Matrix = \n ", confusion_matrix(Y_test, y_pred))

# Display detailed classification report: precision, recall, f1-score for each class
print("\nClassification Report = \n", classification_report(Y_test, y_pred))

# Predict the class for a new sample data point
x_new = [[5, 5, 4, 4]]  # Example features
y_new = gnb.predict(x_new)
print("Predicted output for [[5,5,4,4]] = ", y_new)
