import sympy as sp

if __name__ == "__main__":
    # STEP 1 (CANDIADTE SOLUTIONS REPRESENTATION)
    bits = int(input("Enter the no of bits to represent a candidate solution : "))
    while(bits<=0):
        print("Enter valid integer value!")
        bits = int(input("Enter the no of bits to represent a candidate solution : "))

    # STEP 2 (GROUP OF CANDIDATE SOLUTIONS)
    while True:
        population_input = input(f"Enter all {bits}-bits candidate solutions (comma-separated): ")
        population = [
            chromosome.strip()
            for chromosome in population_input.split(",")
        ]

        if not population or any(chromosome == "" for chromosome in population):
            print("Population cannot be empty.")
            continue

        invalid_chromosomes = []
        for chromosome in population:
            if len(chromosome) != bits:
                invalid_chromosomes.append(f"{chromosome} (must contain exactly {bits} bits)")
            elif any(bit not in "01" for bit in chromosome):
                invalid_chromosomes.append(f"{chromosome} (must contain only 0 and 1)")

        if invalid_chromosomes:
            print("\nInvalid chromosome(s):")
            for chromosome in invalid_chromosomes:
                print(" -", chromosome)
            print("\nPlease enter the population again.")
            continue

        break

    # STEP 3 (FITNESS FUNCTION -> FITNESS SCORE)
    function_input = input("Enter fitness function (in terms of x) : ")
    x = sp.symbols('x')
    fitness_function = sp.sympify(function_input)

    fitness_scores = []
    for chromosome in population:
        c_x = int(chromosome, 2)
        fitness_score = fitness_function.subs(x,c_x)
        fitness_scores.append(fitness_score)
    
    # STEP 4 (SELECTION)
    select_count = int(input("Enter the number of individuals to select as PARENTS : "))
    while(select_count > len(population)):
        print("Select valid no of parents among given population!")
        select_count = int(input("Enter the number of individuals to select as PARENTS : "))

    sorted_pairs = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
    parents = sorted_pairs[:select_count]

    # STEP 5 (CROSSOVER)
    offsprings = set()
    choice = input("Want to perform crossover of parents? (y/n) : ")

    if select_count < 2:
        print("Atleast 2 parents are required for CROSSOVER.")
    else:
        while choice.lower() == "y":
            parent1 = int(input("Select Parent 1 : "))
            while parent1 < 1 or parent1 > select_count:
                print("Select valid parent!")
                parent1 = int(input("Select Parent 1 : "))

            parent2 = int(input("Select Parent 2 : "))
            while parent2 < 1 or parent2 > select_count:
                print("Select valid parent!")
                parent2 = int(input("Select Parent 2 : "))

            if parent1 == parent2:
                print("Parent 1 and Parent 2 cannot be the same!")
                continue

            while True:
                crossover_points = list(
                    map(int,input(f"Enter the crossover points between P{parent1} & P{parent2} (comma-separated) : ").split(",")
                    )
                )

                invalid = False
                for point in crossover_points:
                    if point < 1 or point >= bits:
                        invalid = True
                        break

                if invalid:
                    print(f"Enter valid crossover points (1 to {bits-1})!")
                    continue

                if len(crossover_points) != len(set(crossover_points)):
                    print("Crossover points cannot be duplicated!")
                    continue

                crossover_points.sort()
                break

            chromosome1 = parents[parent1-1][0]
            chromosome2 = parents[parent2-1][0]

            points = [0] + crossover_points + [bits]
            offspring1 = ""
            offspring2 = ""

            # Multi-point crossover
            for i in range(len(points) - 1):
                start = points[i]
                end = points[i+1]
                if i % 2 == 0:
                    offspring1 += chromosome1[start:end]
                    offspring2 += chromosome2[start:end]
                else:
                    offspring1 += chromosome2[start:end]
                    offspring2 += chromosome1[start:end]

            offsprings.add(offspring1)
            offsprings.add(offspring2)

            choice = input("Want to perform another crossover? (y/n) : ")

    # STEP 6 (MUTATION)
    choice = input("Want to perform Mutation of parents? (y/n) : ")

    if select_count < 1:
        print("Atleast 1 parent is required for MUTATION.")
    else:
        while choice.lower() == "y":
            parent = int(input("Select Parent for Mutation : "))

            while parent < 1 or parent > select_count:
                print("Select valid parent!")
                parent = int(input("Select Parent for Mutation : "))

            chromosome = parents[parent-1][0]
            mutation_point = int(input(f"Enter the mutation point for P{parent} (1 to {bits}) : "))

            while mutation_point < 1 or mutation_point > bits:
                print(f"Enter valid mutation point (1 to {bits})!")
                mutation_point = int(input(f"Enter the mutation point for P{parent} (1 to {bits}) : "))

            chromosome_list = list(chromosome)
            index = mutation_point - 1

            if chromosome_list[index] == "0":
                chromosome_list[index] = "1"
            else:
                chromosome_list[index] = "0"

            mutated_chromosome = "".join(chromosome_list)
            offsprings.add(mutated_chromosome)

            choice = input("Want to perform another mutation? (y/n) : ")

    # STEP 7 (DISPLAY OFFSPRING)
    print("\nFinal Offsprings:")
    if offsprings:
        for i, offspring in enumerate(offsprings, start=1):
            print(f"Offspring {i} : {offspring}")
    else:
        print("No offspring generated.")

