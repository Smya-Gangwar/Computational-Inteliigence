def STEPActivation(z):
    return 1 if z >= 0 else 0

def SLP(x1, x2, w1, w2, b):
    z = x1*w1 + x2*w2 + b
    return STEPActivation(z)

if __name__ == "__main__":
    print("SLP Logical AND verification")
    for x1 in range(2):
        for x2 in range(2):
            w1 = 1
            w2 = 1
            b = -1.5
            print(f"x1={x1}, x2={x2} : {SLP(x1, x2, w1, w2, b)}")
