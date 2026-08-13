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

def isvalidConnection(total_layers, prefix, a, b):
    source_layer = None
    dest_layer = None

    for layer in range(total_layers):
        if prefix[layer] < a <= prefix[layer+1]:
            source_layer = layer
        if prefix[layer] < b <= prefix[layer+1]:
            dest_layer = layer

    if dest_layer != source_layer + 1:
        print("Invalid connection! A neuron can only connect to the next layer.")
        return False
    
    return True

def NetworkInput():
    total_layers = int(input("Enter no of hidden layers (Input and Output layers are by default, except those) : "))+2
    neurons = 0
    layers_neurons = []

    for i in range(1,total_layers+1):
        n = int(input(f"Enter the no of neurons in Layer {i} : "))
        layers_neurons.append(n)
        neurons += n
    
    prefix = np.cumsum([0]+layers_neurons)
    connections = np.zeros((neurons, neurons), dtype=int)
    while True:
        a = int(input("Enter source neuron : "))
        b = int(input("Enter destination neuron : "))
        if(isvalidConnection(total_layers, prefix, a, b)):
            connections[a-1][b-1] = 1
        choice = int(input("New connection? (0-No/1-Yes) : "))
        if choice == 0:
            break
    
    weight_neurons = []
    bias_neurons = []
    transposed = connections.T
    for neuron in range(neurons):
        neuron_connections = np.sum(transposed[neuron])
        weights = list(map(float,input(f"Enter {neuron_connections} weight values for Neuron {neuron+1} (comma-separated) : ").split(",")))
        weight_neurons.append(weights)
        bias_neurons.append(float(input(f"Enter bias for Neuron {neuron+1} : ")))
    
    activationFn = None
    while True:
        print(f"Choose Activation function for the ANN.")
        print("1. STEP")
        print("2. SIGMOID")
        print("3. TANH")
        print("4. RELU")
        print("5. Leaky RELU")
        print("6. ELU")
        choice = int(input("Enter (1-6) : "))

        if choice == 1:
            activationFn = STEPActivation
            break
        elif choice == 2:
            activationFn = SigmoidActivation
            break
        elif choice == 3:
            activationFn = TanhActivation
            break
        elif choice == 4:
            activationFn = ReluActivation
            break
        elif choice == 5:
            activationFn = LeakyReluActivation
            break
        elif choice == 6:
            activationFn = ELUActivation
            break
        else:
            print("Wrong choice! Choose Again")
    
    learning_rate = float(input("Enter the ANN learning rate : "))
    convergence_threshold = float(input("Enter the ANN convergence threshold : "))
    epochs = int(input("Enter maximum epochs for training ANN : "))
    
    return total_layers, layers_neurons, connections, weight_neurons, bias_neurons, activationFn, learning_rate, convergence_threshold, epochs

if __name__=="__main__":
    total_layers, layers_neurons, connections, weight_neurons, bias_neurons, activationFn, learning_rate, convergence_threshold, epochs = NetworkInput()
