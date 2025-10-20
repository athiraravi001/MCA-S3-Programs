# To implement KNN classification using any standard dataset available in the public domain (Iris Dataset), and find the accuracy of the algorithm.

import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ===== Step 1: Load dataset =====
df = pd.read_csv(".venv/DataSet/Iris.csv")

# ===== Step 2: Separate features and target =====
X = df.iloc[:, 1:5]   # Features: SepalLength, SepalWidth, PetalLength, PetalWidth
y = df.iloc[:, -1]    # Target: Species (labels)
print("Features sample = \n", X.head(),"\n")  # Show first 5 rows of features
print("Target sample = \n", y.head(),"\n")    # Show first 5 rows of target

# ===== Step 3: Split dataset into training and testing (70% training, 30% testing) =====
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
print("Training set shape :", X_train.shape, y_train.shape)
print("Testing set shape :", X_test.shape, y_test.shape,"\n")

# ===== Step 4: Identify the ideal value for k (number of neighbors) =====
scores = []
for k in range(5, 15):
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)  # Create KNN model with k neighbors
    knn.fit(X_train, y_train)                            # Train model on training data
    y_pred = knn.predict(X_test)                         # Predict test set labels
    scores.append([k, accuracy_score(y_test, y_pred)])   # Store accuracy for this k
    print("When k = %s, Accuracy = %.4f" % (k, accuracy_score(y_test, y_pred)))

# Find best k based on highest accuracy
max_value = max(x[1] for x in scores)                  # Maximum accuracy achieved
best_k = [x[0] for x in scores if x[1] == max_value]   # All k values with max accuracy
best_k = min(best_k)  # choose smallest k if there is a tie
print("\nBest k value =", best_k)

# ===== Step 5: Train final model with best_k =====
knn = neighbors.KNeighborsClassifier(n_neighbors=best_k)  # Final model with best k
knn.fit(X_train, y_train)                                 # Train on full training set
y_pred_final = knn.predict(X_test)                        # Predict test set

# ===== Step 6: Evaluate final model =====
print("\nFinal Model Accuracy = {:.2f}%".format(accuracy_score(y_test, y_pred_final)*100))
print("\nConfusion Matrix = \n", confusion_matrix(y_test, y_pred_final))
print("\nClassification Report = \n", classification_report(y_test, y_pred_final))