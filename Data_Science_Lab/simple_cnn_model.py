# ===== Import necessary libraries =====
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical

# ===== Load the MNIST dataset =====
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Print shapes of training and test data
print("Training data shape:", x_train.shape)  # (60000, 28, 28)
print("Testing data shape:", x_test.shape)    # (10000, 28, 28)

# ===== Preprocess the data =====
# Reshape the data to include a single channel (grayscale)
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# Normalize pixel values to the range [0, 1] for faster convergence
x_train = x_train / 255.0
x_test = x_test / 255.0

# Print some sample labels before encoding
print("Sample training labels (before one-hot encoding):", y_train)

# Convert integer labels to one-hot encoding
# Example: 3 → [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# ===== Create the Sequential CNN model =====
model = Sequential()

# Convolutional layer: extract features using 32 filters of size 3x3
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28,28,1)))

# Max pooling layer: reduce spatial dimensions to prevent overfitting and reduce computation
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the 2D feature maps into a 1D vector for dense layers
model.add(Flatten())

# Fully connected (dense) layer: 128 neurons with ReLU activation
model.add(Dense(128, activation='relu'))

# Output layer: 10 neurons (one per digit) with softmax activation for multi-class classification
model.add(Dense(10, activation='softmax'))

# ===== Compile the model =====
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model layers and parameters
model.summary()

# ===== Train the model =====
print("\nTraining the model...")
model.fit(x_train, y_train,
          epochs=5, batch_size=64, validation_data=(x_test, y_test))

# ===== Evaluate the model =====
loss, accuracy = model.evaluate(x_test, y_test)
print(f"\nTest Loss : {loss:.4f}, Test Accuracy: {accuracy:.4f}")

# ===== Predict on a single sample =====
x = np.expand_dims(x_test[20], axis=0)  # Add batch dimension: (1, 28, 28, 1)
print("\nInput shape for prediction :", x.shape)

# Make prediction
output = model.predict(x)

# Print rounded probabilities for each class (0-9)
print("\nPrediction probabilities (rounded) : ", np.round(output, decimals=2))