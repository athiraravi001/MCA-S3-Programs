# To implement multiple linear regression to predict relative humidity using AirQuality dataset

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load the dataset from the given CSV file
df = pd.read_csv(".venv/DataSet/AirQuality.csv")

# Define the feature matrix (X) and target variable (y)
x = df.iloc[:, 2:13]        # Selecting columns 2 to 12 as input features (i.e., predictors)
y = df.iloc[:, 13:14]       # Selecting column 13 (relative humidity) as the target variable

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=41)

# Create a Linear Regression model instance
lr = LinearRegression()

# Train the model on the training data
lr.fit(x_train, y_train)

# Print the intercept and slope (coefficients) of the model
print("Intercept =", lr.intercept_)     # This is the bias term
print("Slope =\n", lr.coef_)            # These are the weights for each input feature

# Predict the target variable for both training and testing sets
train_pred = lr.predict(x_train)
test_pred = lr.predict(x_test)

# ----------- Evaluation on Training Set -----------
print("\n===== Training performance =====")
print("R.squared: ", r2_score(y_train, train_pred))
print("Mean squared error: ", mean_squared_error(y_train, train_pred))
print("Root mean squared error: ", np.sqrt(mean_squared_error(y_train, train_pred)))
print("Mean absolute error: ", mean_absolute_error(y_train, train_pred))

# ----------- Evaluation on Testing Set -----------
print("\n===== Testing performance =====")
print("R.squared: ", r2_score(y_test, test_pred))
print("Mean squared error: ", mean_squared_error(y_test, test_pred))
print("Root mean squared error: ", np.sqrt(mean_squared_error(y_test, test_pred)))
print("Mean absolute error :", mean_absolute_error(y_test, test_pred))
