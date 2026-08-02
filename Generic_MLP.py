import sys
import numpy as np

def STEPActivation(z):
    return 1 if z >= 0 else 0

def SigmoidActivation(z):
    return 1 / (1 + np.exp(-z))

def TanhActivation(z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

def ReluActivation(z):
    return max(0, z)

def LeakyReluActivation(z):
    # alpha = 0.01
    return z if z > 0 else 0.01 * z

def ELUActivation(z):
    # alpha = 1
    return z if z > 0 else 1*(np.exp(z) - 1)

def SLP(inputs, weights, bias, activationFn):
    output = []
    for ip in inputs:
        z = sum(i*w for i,w in zip(ip, weights)) + bias
        output.append(activationFn(z))
    return output

def forwardLayer(inputs, weights_list, bias_list, activationFn):
    output = []
    for weights, bias in zip(weights_list, bias_list):
        output.append(SLP(inputs, weights, bias, activationFn))
    inputs = np.array(output).T
    return inputs

if __name__ == "__main__":
    raw_input = input("Enter inputs (comma-separated) and input-sets (semicolon-separated): ")
    inputs = [list(map(float, s.strip().split(','))) for s in raw_input.split(';')]

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

        print(f"Choose Activation function for {term} layer {layer} :")
        print("1. STEP")
        print("2. SIGMOID")
        print("3. TANH")
        print("4. RELU")
        print("5. Leaky RELU")
        print("6. ELU")
        choice = int(input("Enter (1-6) : "))

        activationFn = None
        if choice == 1:
            activationFn = STEPActivation
        elif choice == 2:
            activationFn = SigmoidActivation
        elif choice == 3:
            activationFn = TanhActivation
        elif choice == 4:
            activationFn = ReluActivation
        elif choice == 5:
            activationFn = LeakyReluActivation
        elif choice == 6:
            activationFn = ELUActivation
        else:
            print("Wrong choice!")
            sys.exit(1)

        hidden_outputs = forwardLayer(inputs, weights_list, bias_list, activationFn)
        for i, sample in enumerate(hidden_outputs):
            print(f"Input {inputs[i]} -> {sample}")

        inputs = hidden_outputs