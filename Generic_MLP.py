import numpy as np

def STEPActivation(z):
    return 1 if z >= 0 else 0

def SLP(inputs, weights, bias):
    output = []
    for ip in inputs:
        z = sum(i*w for i,w in zip(ip, weights)) + bias
        output.append(STEPActivation(z))
    return output

def forwardLayer(inputs, weights_list, bias_list):
    output = []
    for weights, bias in zip(weights_list, bias_list):
        output.append(SLP(inputs, weights, bias))
    inputs = np.array(output).T
    return inputs

if __name__ == "__main__":
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    layers = int(input("Enter number of hidden layers: "))
    for layer in range(1, layers + 2):
        term = "hidden"
        if(layer == layers+1):
            term = "output"

        print(f"Enter weights for {term} layer {layer}:")
        weights_list = [np.array(
            list(map(float, s.split(",")))) 
            for s in input("Enter weights (semicolon-separated): ").split(";")
        ]

        print(f"Enter biases for {term} layer {layer}:")
        bias_list = list(
            map(float, input("Enter biases (comma-separated): ").split(","))
        )

        hidden_outputs = forwardLayer(inputs, weights_list, bias_list)
        for i, sample in enumerate(hidden_outputs):
            print(f"Input {inputs[i]} -> {sample}")
            
        inputs = hidden_outputs