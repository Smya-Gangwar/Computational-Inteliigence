import numpy as np

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
    connections = [[0 for _ in range(neurons)] for _ in range(neurons)]
    while True:
        a = int(input("Enter source neuron : "))
        b = int(input("Enter destination neuron : "))
        if(isvalidConnection(total_layers, prefix, a, b)):
            connections[a-1][b-1] = 1
        choice = int(input("New connection? (0-No/1-Yes) : "))
        if choice == 0:
            break
    
    return total_layers, layers_neurons, connections

if __name__=="__main__":
    total_layers, layers_neurons, connections = NetworkInput()
    