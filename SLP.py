import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[1]])

# Initial weights and bias
np.random.seed(1)
W = np.random.uniform(-1,1,(2,1))
B = np.random.uniform(-1,1,(1,1))

learning_rate = 0.1
epochs = 10000
convergence_threshold = 0.001

for epoch in range(epochs):
    # Forward propagation
    z = np.dot(X, W) + B
    y_pred = sigmoid(z)

    # Error
    error = Y - y_pred
    MSE = np.mean(error**2)/2

    if MSE < convergence_threshold:
        print(f"Converged at epoch {epoch}")
        print(f"MSE = {MSE:.6f}")
        break

    # Backpropagation
    # delta = error * sigmoid derivative
    delta = error * sigmoid_derivative(y_pred)

    # Weight update
    W += learning_rate * np.dot(X.T, delta)
    B += learning_rate * np.sum(delta, axis=0, keepdims=True)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, MSE = {MSE:.6f}")


print("\nFinal weights")
print(W)

print("\nFinal bias")
print(B)

# Testing
output = sigmoid(np.dot(X,W)+B)
print("\nPredictions")
for i in range(len(X)):
    prediction = 1 if output[i] >= 0.5 else 0
    print(X[i], "->", output[i][0], "->", prediction)