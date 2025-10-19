import numpy as np

inputs = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
outputs = np.array([1, -1, -1, -1])  # AND gate truth table

# Initialise weights and bias
weights = np.zeros(2)  # 2 inputs, so 2 weights
bias = 0
learning_rate = 1
threshold = 0

# Perceptron learning algorithm
for epoch in range(5):
    print(f"\n\n{'*' * 30} Epoch {epoch + 1} {'*' * 30}")
    for i in range(len(inputs)):
        print(f"\nInput Pattern {i + 1}: {inputs[i]}")

        # Calculate the weighted sum
        weighted_sum = np.dot(inputs[i], weights) + bias
        print(f"   -> Weighted Sum      : {weighted_sum:.2f}")

        # Apply the step activation function
        if weighted_sum > 0:
            prediction = 1
        elif weighted_sum < 0:
            prediction = -1
        elif weighted_sum == 0:
            prediction = 0

        # Calculate the error
        error = outputs[i] - prediction

        # Update weights and bias
        if error != 0:
            weights += learning_rate * error * inputs[i]
            bias += learning_rate * error

        # Display details
        print(f"   -> Target Output (y) : {outputs[i]}")
        print(f"   -> Prediction        : {prediction}")
        print(f"   -> Error             : {error}")
        print(f"   -> Updated Weights   : {weights}")
        print(f"   -> Updated Bias      : {bias}")
        print("-" * 80)

# Final Results after training
print(f"\n\n{'=' * 35} Training Complete {'=' * 35}")
print(f"Final Weights : {weights}")
print(f"Final Bias    : {bias}")
print(f"Total Epochs  : {epoch + 1}")