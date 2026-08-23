import numpy as np

def STEPActivation(z):
    return 1 if z >= 0 else 0

def STEPDerivative(z):
    return 0

def SigmoidActivation(z):
    return 1 / (1 + np.exp(-z))

def SigmoidDerivative(z):
    a = SigmoidActivation(z)
    return a * (1 - a)

def TanhActivation(z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

def TanhDerivative(z):
    a = TanhActivation(z)
    return 1 - a**2

def ReluActivation(z):
    return max(0, z)

def ReluDerivative(z):
    return 1 if z > 0 else 0

def LeakyReluActivation(z):
    # alpha = 0.01
    return z if z > 0 else 0.01 * z

def LeakyReluDerivative(z):
    return 1 if z > 0 else 0.01

def ELUActivation(z):
    # alpha = 1
    return z if z > 0 else 1*(np.exp(z) - 1)

def ELUDerivative(z):
    return 1 if z > 0 else np.exp(z)

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
    
    weight_neurons = [None]*prefix[1]
    bias_neurons = [None]*prefix[1]
    transposed = connections.T
    # All layer 1 neurons are not actual neurons but Input neurons
    for neuron in range(prefix[1], neurons):
        neuron_connections = np.sum(transposed[neuron])
        while True:
            weights = list(map(float,input(f"Enter {neuron_connections} weight values for Neuron {neuron+1} (comma-separated) : ").split(",")))
            if len(weights) == neuron_connections:
                weight_neurons.append(weights)
                break
            else:
                print(f"Please enter exactly {neuron_connections} weights.")
        bias_neurons.append(float(input(f"Enter bias for Neuron {neuron+1} : ")))
    
    activationFn = None
    activationDerivative = None
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
            activationDerivative = STEPDerivative
            break
        elif choice == 2:
            activationFn = SigmoidActivation
            activationDerivative = SigmoidDerivative
            break
        elif choice == 3:
            activationFn = TanhActivation
            activationDerivative = TanhDerivative
            break
        elif choice == 4:
            activationFn = ReluActivation
            activationDerivative = ReluDerivative
            break
        elif choice == 5:
            activationFn = LeakyReluActivation
            activationDerivative = LeakyReluDerivative
            break
        elif choice == 6:
            activationFn = ELUActivation
            activationDerivative = ELUDerivative
            break
        else:
            print("Wrong choice! Choose Again")
    
    learning_rate = float(input("Enter the ANN learning rate : "))
    convergence_threshold = float(input("Enter the ANN convergence threshold : "))
    epochs = int(input("Enter maximum epochs for training ANN : "))

    return (total_layers, layers_neurons, connections, weight_neurons, bias_neurons, activationFn, activationDerivative, learning_rate,
            convergence_threshold, epochs)

def TrainingDataInput(input_neurons, output_neurons):
    n = int(input("Enter the number of training data sets : "))
    training_data = []
    for i in range(n):
        while True:
            data = list(map(float, input(f"Enter input values for training set {i+1} (comma-separated) : ").split(",")))
            if len(data) != input_neurons:
                print(f"Please enter exactly {input_neurons} input values.")
            else:
                break
        while True:
            label = list(map(float, input(f"Enter output values for training set {i+1} (comma-separated) : ").split(",")))
            if len(label) != output_neurons:
                print(f"Please enter exactly {output_neurons} output values.")
            else:
                break
        training_data.append((data, label))
    return training_data

def ForwardPropagation(training_data, layers_neurons, connections, weight_neurons, bias_neurons, activationFn):
    neurons = len(connections)
    prefix = np.cumsum([0] + layers_neurons)

    predicted_output = []
    all_activations = []
    all_z_values = []

    for data, _ in training_data:
        activations = [None] * neurons
        z_values = [None] * neurons

        # Input layer = raw input values
        for i in range(layers_neurons[0]):
            activations[i] = data[i]

        # Hidden + output layers
        for layer in range(1, len(layers_neurons)):
            start_neuron = prefix[layer]
            end_neuron = prefix[layer + 1]

            for destination in range(start_neuron, end_neuron):
                z = bias_neurons[destination]
                weight_index = 0

                previous_layer_start = prefix[layer - 1]
                previous_layer_end = prefix[layer]

                for source in range(previous_layer_start, previous_layer_end):
                    if connections[source][destination] == 1:
                        weight = weight_neurons[destination][weight_index]
                        z += activations[source] * weight
                        weight_index += 1

                z_values[destination] = z
                activations[destination] = activationFn(z)

        output_start = prefix[-2]
        output_end = prefix[-1]
        output = activations[output_start:output_end]

        predicted_output.append(output)
        all_activations.append(activations)
        all_z_values.append(z_values)

    return predicted_output, all_activations, all_z_values

def CalculateError(predicted_output, training_data):
    # MSE - Mean Squared Error
    losses = 0
    for prediction, (_, label) in zip(predicted_output, training_data):
        error = np.array(label) - np.array(prediction)
        losses += np.sum(error ** 2)/2
    losses /= len(training_data)
    return losses

def CalculateOutputDeltas(prediction, label, z_values, layers_neurons, activationDerivative):
    prefix = np.cumsum([0] + layers_neurons)

    output_start = prefix[-2]
    output_end = prefix[-1]
    deltas = [None] * len(z_values)

    for neuron in range(output_start, output_end):
        output_index = neuron - output_start
        a = prediction[output_index]
        y = label[output_index]
        deltas[neuron] = ((a - y) * activationDerivative(z_values[neuron]))

    return deltas

def GetConnectionWeight(source, destination, layers_neurons, connections, weight_neurons):
    prefix = np.cumsum([0] + layers_neurons)
    for layer in range(len(layers_neurons)):
        if prefix[layer] <= source < prefix[layer + 1]:
            source_layer = layer
            break

    weight_index = 0
    start = prefix[source_layer]
    end = prefix[source_layer + 1]

    for current_source in range(start, end):
        if connections[current_source][destination] == 1:
            if current_source == source:
                return weight_neurons[destination][weight_index]
            weight_index += 1

    return None

def CalculateHiddenDeltas(deltas, z_values, layers_neurons, connections, weight_neurons, activationDerivative):
    prefix = np.cumsum([0] + layers_neurons)

    for layer in range(len(layers_neurons) - 2, 0, -1):
        current_start = prefix[layer]
        current_end = prefix[layer + 1]
        next_start = prefix[layer + 1]
        next_end = prefix[layer + 2]

        for neuron in range(current_start, current_end):
            weighted_delta_sum = 0
            for destination in range(next_start, next_end):
                if connections[neuron][destination] == 1:
                    weight = GetConnectionWeight(neuron, destination, layers_neurons, connections, weight_neurons)
                    weighted_delta_sum += (weight * deltas[destination])

            deltas[neuron] = (weighted_delta_sum * activationDerivative(z_values[neuron]))

    return deltas

def BackPropagation(prediction, label, z_values, layers_neurons, connections, weight_neurons, activationDerivative):
    deltas = [None] * len(connections)

    # Output layer
    deltas = CalculateOutputDeltas(
        prediction,
        label,
        z_values,
        layers_neurons,
        activationDerivative
    )

    # Hidden layers
    deltas = CalculateHiddenDeltas(
        deltas,
        z_values,
        layers_neurons,
        connections,
        weight_neurons,
        activationDerivative
    )

    return deltas

def CalculateGradients(activations, deltas, layers_neurons, connections):
    prefix = np.cumsum([0] + layers_neurons)
    weight_gradients = [None] * len(deltas)
    bias_gradients = [None] * len(deltas)

    for neuron in range(prefix[1], len(deltas)):
        weight_gradients[neuron] = []
        bias_gradients[neuron] = deltas[neuron]

    for layer in range(1, len(layers_neurons)):
        current_start = prefix[layer]
        current_end = prefix[layer + 1]
        previous_start = prefix[layer - 1]
        previous_end = prefix[layer]

        for destination in range(current_start, current_end):
            for source in range(previous_start, previous_end):
                if connections[source][destination] == 1:
                    gradient = (activations[source] * deltas[destination])
                    weight_gradients[destination].append(gradient)

    return weight_gradients, bias_gradients

def UpdateParameters(weight_neurons, bias_neurons, weight_gradients, bias_gradients, learning_rate):
    for neuron in range(len(weight_neurons)):
        if weight_neurons[neuron] is None:
            continue

        for i in range(len(weight_neurons[neuron])):
            weight_neurons[neuron][i] -= ( learning_rate * weight_gradients[neuron][i] )

        bias_neurons[neuron] -= ( learning_rate * bias_gradients[neuron] )

if __name__=="__main__":
    (total_layers, layers_neurons, connections, weight_neurons, bias_neurons, activationFn, activationDerivative, learning_rate, 
    convergence_threshold, epochs) = NetworkInput()
    training_data = TrainingDataInput(layers_neurons[0], layers_neurons[-1])

    # SGD training (per training sample)
    print("\nStarting training..\n")
    for epoch in range(epochs):
        epoch_loss = 0
        for data, label in training_data:
            sample_data = [(data, label)]
            predicted_output, all_activations, all_z_values = ForwardPropagation(
                sample_data,
                layers_neurons,
                connections,
                weight_neurons,
                bias_neurons,
                activationFn
            )

            prediction = predicted_output[0]
            activations = all_activations[0]
            z_values = all_z_values[0]

            sample_loss = CalculateError(
                predicted_output,
                sample_data
            )
            epoch_loss += sample_loss

            # Backpropagation
            deltas = BackPropagation(
                prediction,
                label,
                z_values,
                layers_neurons,
                connections,
                weight_neurons,
                activationDerivative
            )

            # Calculate gradients
            weight_gradients, bias_gradients = CalculateGradients(
                activations,
                deltas,
                layers_neurons,
                connections
            )

            # Update parameters
            UpdateParameters(
                weight_neurons,
                bias_neurons,
                weight_gradients,
                bias_gradients,
                learning_rate
            )

        # Average loss for the epoch
        epoch_loss /= len(training_data)
        print(f"Epoch {epoch + 1}/{epochs} | Loss = {epoch_loss:.6f}")

        # Convergence
        if epoch_loss <= convergence_threshold:
            print("\nConvergence achieved!")
            break

    print("\nTraining completed.")
    final_predictions, _, _ = ForwardPropagation(
        training_data,
        layers_neurons,
        connections,
        weight_neurons,
        bias_neurons,
        activationFn
    )

    print("\nFinal Predictions:")
    for i, ((data, label), prediction) in enumerate(zip(training_data, final_predictions)):
        print(f"Sample {i + 1} : Input = {data}, Actual = {label}, Predicted = {prediction}")

    # Final loss
    final_loss = CalculateError(final_predictions, training_data)
    print(f"\nFinal Loss = {final_loss:.6f}")