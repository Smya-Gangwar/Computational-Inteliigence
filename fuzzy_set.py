import random

def get_universe():
    n = int(input("Enter size of universe of discourse: "))
    uod = []
    for i in range(n):
        val = input(f"Enter element {i+1}: ")
        uod.append(val)
    return uod

def random_membership(uod, set_name):
    values = [round(random.uniform(0, 1), 2) for _ in uod]
    print(f"\nMembership values for {set_name}:")
    for u, v in zip(uod, values):
        print(f"{u} : {v}")
    return values

def display_set(uod, values, name):
    print(name)
    for u, v in zip(uod, values):
        print(f"{u} : {v}")

def complement(values):
    return [round(1-v, 2) for v in values]

def union(valuesA, valuesB):
    return [max(a,b) for a, b in zip(valuesA, valuesB)]

def intersection(valuesA, valuesB):
    return [min(a,b) for a, b in zip(valuesA, valuesB)]

def main():
    uod = get_universe()
    A = random_membership(uod, "Set A")
    B = random_membership(uod, "Set B")

    while True:
        print("\nMenu:")
        print("1. Complement of A")
        print("2. Complement of B")
        print("3. A union B")
        print("4. A intersection B")
        print("5. All operations")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            display_set(uod, complement(A), "Complement of A")
        elif choice == "2":
            display_set(uod, complement(B), "Complement of B")
        elif choice == "3":
            display_set(uod, union(A, B), "A UNION B")
        elif choice == "4":
            display_set(uod, intersection(A, B), "A INTERSECTION B")
        elif choice == "5":
            display_set(uod, complement(A), "Complement of A")
            display_set(uod, complement(B), "Complement of B")
            display_set(uod, union(A, B), "A UNION B")
            display_set(uod, intersection(A, B), "A INTERSECTION B")
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
