import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[0]])
learning_rate = 0.5
epochs = 20000

convergence_threshold = 0.005

# Initial weights and biases
np.random.seed(42)
W1 = np.random.uniform(-1,1,(2,2))
B1 = np.random.uniform(-1,1,(1,2))
W2 = np.random.uniform(-1,1,(2,1))
B2 = np.random.uniform(-1,1,(1,1))

for epoch in range(epochs):
    # Forward Pass
    hidden_input = np.dot(X, W1) + B1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + B2
    final_output = sigmoid(final_input)

    # Error & Backpropogation
    error = Y - final_output
    MSE = np.mean(error**2)/2

    if MSE < convergence_threshold:
        print(f"\nTraining Converged!")
        print(f"Epoch : {epoch}")
        print(f"MSE : {MSE:.6f}")
        break

    delta_output = error * sigmoid_derivative(final_output)
    hidden_error = np.dot(delta_output, W2.T)
    delta_hidden = hidden_error * sigmoid_derivative(hidden_output)

    # Update Weights 
    W2 += learning_rate * np.dot(hidden_output.T, delta_output)
    B2 += learning_rate * np.sum(delta_output, axis=0, keepdims=True)

    W1 += learning_rate * np.dot(X.T, delta_hidden)
    B1 += learning_rate * np.sum(delta_hidden, axis=0, keepdims=True)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch:5d}  Loss = {MSE:.6f}")

print("\nTraining Complete\n")

print("Hidden Layer Weights:")
print(W1)

print("\nHidden Layer Bias:")
print(B1)

print("\nOutput Layer Weights:")
print(W2)

print("\nOutput Layer Bias:")
print(B2)

print("\nPredictions:")
hidden_output = sigmoid(np.dot(X, W1) + B1)
final_output = sigmoid(np.dot(hidden_output, W2) + B2)
for i in range(len(X)):
    pred = 1 if final_output[i][0] >= 0.5 else 0
    print(f"{X[i]} -> {final_output[i][0]:.4f} -> {pred}")