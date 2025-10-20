# To implement linear regression techniques using Insurance Dataset and evaluate its performance

# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load the dataset
df = pd.read_csv(".venv/DataSet/Insurance.csv")  # Load the insurance data from CSV

# Display first five rows to get an idea of the data
print(df.head(),"\n")

# Check for missing values in the dataset
print(df.isnull().sum())

# Select the independent and dependent variables
x = df.iloc[:, 0:1]  # Selecting the first column as feature (independent variable)
y = df.iloc[:, -1]   # Selecting the last column as target (dependent variable)

# Split the dataset into training and test sets (67% training, 33% testing)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)

print("\n=== Shapes of Train/Test Data ===")
print(f"x_train: {x_train.shape}, y_train: {y_train.shape}")
print(f"x_test : {x_test.shape}, y_test : {y_test.shape}\n")

# Create Linear Regression model
lr = LinearRegression()

# Train the model using training data
lr.fit(x_train, y_train)

# Print model coefficients (intercept and slope)
print("Intercept:", lr.intercept_)
print("Slope :", lr.coef_)

# Predict values for both training and test data
train_pred = lr.predict(x_train)
test_pred = lr.predict(x_test)

# Evaluate model performance on training data
print(f"\n===== Training Set =====")
print(f"R.squared: {r2_score(y_train, train_pred):.3f}")
print(f"Mean squared error: {mean_squared_error(y_train, train_pred):.3f}")
print(f"Root mean squared error: {np.sqrt(mean_squared_error(y_train, train_pred)):.3f}")
print(f"Mean absolute error: {mean_absolute_error(y_train, train_pred):.3f}")

# Evaluate model performance on test data
print(f"\n===== Testing Set =====")
print(f"R.squared: {r2_score(y_test, test_pred):.3f}")
print(f"Mean squared error: {mean_squared_error(y_test, test_pred):.3f}")
print(f"Root mean squared error: {np.sqrt(mean_squared_error(y_test, test_pred)):.3f}")
print(f"Mean absolute error: {mean_absolute_error(y_test, test_pred):.3f}")

# Plot a regression line with seaborn
sb.regplot(x=x, y=y)  # This will show the regression line for the entire dataset
plt.show()