import numpy as np

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

# XOR Input and Target
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Network Architecture: 2 inputs -> 2 hidden neurons -> 1 output neuron
np.random.seed(42)
input_dim, hidden_dim, output_dim = 2, 2, 1
lr = 0.5
epochs = 10000

# Initialize weights and biases
W_h = np.random.uniform(size=(input_dim, hidden_dim))
b_h = np.random.uniform(size=(1, hidden_dim))
W_o = np.random.uniform(size=(hidden_dim, output_dim))
b_o = np.random.uniform(size=(1, output_dim))

# Training Loop
for epoch in range(epochs):
    # Forward Pass
    hidden_input = np.dot(X, W_h) + b_h
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, W_o) + b_o
    final_output = sigmoid(final_input)

    # Backpropagation
    error = y - final_output
    d_output = error * sigmoid_derivative(final_output)

    hidden_error = d_output.dot(W_o.T)
    d_hidden = hidden_error * sigmoid_derivative(hidden_output)

    # Gradient Updates
    W_o += hidden_output.T.dot(d_output) * lr
    b_o += np.sum(d_output, axis=0, keepdims=True) * lr
    W_h += X.T.dot(d_hidden) * lr
    b_h += np.sum(d_hidden, axis=0, keepdims=True) * lr

print("--- XOR Gate (Backpropagation) Predictions ---")
for xi, target, pred in zip(X, y, final_output):
    print(f"Input: {xi} -> Raw Output: {pred[0]:.4f} -> Class: {round(pred[0])} (Target: {target[0]})")

print("Name: Prasanna Pokharel")
print("Rollno: 24")
print("LAB IV-2")