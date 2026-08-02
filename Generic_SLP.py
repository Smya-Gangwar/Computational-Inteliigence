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
    z = sum(i*w for i,w in zip(inputs, weights)) + bias
    return activationFn(z)

if __name__ == "__main__":
    raw_input = input("Enter inputs (comma-separated) and input-sets (semicolon-separated): ")
    inputs = [list(map(float, s.strip().split(','))) for s in raw_input.split(';')]
    weights = list(map(float, input("Enter weights (comma-separated) : ").split(',')))
    bias = float(input("Enter bias : "))

    print("Choose Activation function:")
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

    for i, input_set in enumerate(inputs):
        print(f"SLP Output for input set {i+1}:", SLP(input_set, weights, bias, activationFn))