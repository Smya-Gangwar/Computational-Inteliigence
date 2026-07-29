# 2-3-...

import numpy as np

def SigmoidActivation(z):
    return 1 / (1 + np.exp(-z))

def SLP(inputs, weights, bias):
    output = []
    for ip in inputs:
        z = sum(i*w for i,w in zip(ip, weights)) + bias
        output.append(SigmoidActivation(z))
    return output

if __name__ == "__main__":
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    weights = [1, 1]
    bias = -0.5
    h1 = SLP(inputs, weights, bias)
    print("Output of hidden layer 1:", h1)

    weights = [-1, -1]
    bias = 1.5
    h2 = SLP(inputs, weights, bias)
    print("Output of hidden layer 2:", h2)

    inputs = list(zip(h1, h2))
    weights = [1, 1]
    bias = -1.5
    output = SLP(inputs, weights, bias)
    print("Output of output layer:", output)