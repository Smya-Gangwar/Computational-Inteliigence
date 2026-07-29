def STEPActivation(z):
    return 1 if z >= 0 else 0

def SLP(inputs, weights, bias):
    z = sum(i*w for i,w in zip(inputs, weights)) + bias
    return STEPActivation(z)

if __name__ == "__main__":
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    weights = list(map(float, input("Enter weights (comma-separated): ").split(",")))
    bias = float(input("Enter bias: "))
    for i, input_set in enumerate(inputs):
        print(f"SLP Output for input set {i+1}:", SLP(input_set, weights, bias))