import numpy as np
from keras import datasets, layers, models
from keras.datasets import mnist

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

# Preprocess the data
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1) / 255.0
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1) / 255.0

# Build LeNet-5 model
model = models.Sequential([
    layers.Conv2D(6, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)),
    layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2)),
    layers.Conv2D(16, kernel_size=(5, 5), activation='relu'),
    layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2)),
    layers.Flatten(),
    layers.Dense(120, activation='relu'),
    layers.Dense(84, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Summary of the model architecture
print("\n================ Model Summary ================\n")
model.summary()

# Train the model
print("\n================ Training Model ================\n")
model.fit(x_train, y_train, epochs=2, batch_size=64, validation_data=(x_test, y_test))

# Evaluate model
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"\n✅ Test Loss     : {loss:.4f}")
print(f"✅ Test Accuracy : {accuracy:.4f}\n")

# Predict the first test sample
prediction = model.predict(x_test[:1])
predicted_digit = np.argmax(prediction, axis=1)[0]
print(f"Predicted digit for first test image : {predicted_digit}")
print(f"Probabilities : {np.round(prediction, 3)}\n")