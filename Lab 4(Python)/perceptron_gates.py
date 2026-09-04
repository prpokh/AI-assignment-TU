import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=0.1, epochs=20):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.lr = lr
        self.epochs = epochs

    def step_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        # dot product with inputs + bias term
        z = np.dot(x, self.weights[1:]) + self.weights[0]
        return self.step_function(z)

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                output = self.predict(xi)
                error = target - output
                self.weights[1:] += self.lr * error * xi
                self.weights[0] += self.lr * error  # bias update

def evaluate_gate(name, X, y):
    p = Perceptron(input_size=X.shape[1])
    p.train(X, y)
    print(f"--- {name} Gate ---")
    for xi, target in zip(X, y):
        pred = p.predict(xi)
        print(f"Input: {xi} | Predicted: {pred} | Actual: {target}")
    print(f"Weights: {p.weights[1:]}, Bias: {p.weights[0]}\n")

# Datasets
X_2input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])
y_or  = np.array([0, 1, 1, 1])

X_1input = np.array([[0], [1]])
y_not = np.array([1, 0])

evaluate_gate("AND", X_2input, y_and)
evaluate_gate("OR", X_2input, y_or)
evaluate_gate("NOT", X_1input, y_not)

print("Name: Prasanna Pokharel")
print("Rollno: 24")
print("LAB IV-1")