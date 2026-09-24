def get_membership_values():
    memberships = {}
    n = int(input("Enter number of input variables: "))

    for i in range(n):
        variable = input(f"\nEnter name of input variable {i + 1}: ")
        memberships[variable] = {}
        terms = int(input(f"Enter number of membership terms for {variable}: "))
        for j in range(terms):
            term = input(f"Enter membership term {j + 1}: ")
            value = float(input(f"Enter membership value for {variable} = {term}: "))
            memberships[variable][term] = value

    return memberships


def get_output_data():
    print("\nOUTPUT VARIABLE")
    output_name = input("Enter output variable name: ")
    n = int(input("Enter number of values in output universe: "))

    universe = []
    for i in range(n):
        value = float(input(f"Enter output universe value {i + 1}: "))
        universe.append(value)

    output_memberships = {}
    terms = int(input("Enter number of output membership terms: "))

    for i in range(terms):
        term = input(f"\nEnter output membership term {i + 1}: ")
        values = []
        print(f"Enter {n} membership values for {term}:")
        for j in range(n):
            value = float(input(f"  Membership at {universe[j]}: "))
            values.append(value)
        output_memberships[term] = values

    return output_name, universe, output_memberships


def get_rules():
    print("\nRULES")
    n = int(input("Enter number of fuzzy rules: "))

    rules = []
    for i in range(n):
        print(f"\nRule R{i + 1}")
        conditions = {}
        num_conditions = int(input("Enter number of conditions: "))
        for j in range(num_conditions):
            variable = input("Enter input variable: ")
            term = input(f"Enter membership term for {variable}: ")
            conditions[variable] = term
        output_term = input("Enter output membership term: ")
        rules.append((conditions, output_term))

    return rules

def evaluate_rules(memberships, rules, universe, output_memberships):
    rule_outputs = []
    firing_strengths = []

    print("\nRULE EVALUATION")
    for i, (conditions, output_term) in enumerate(rules):
        values = []
        for v, term in conditions.items():
            values.append(memberships[v][term])

        firing_strength = min(values)
        firing_strengths.append(firing_strength)

        modified_output = []
        for value in output_memberships[output_term]:
            modified_output.append(min(firing_strength, value))
        rule_outputs.append(modified_output)

        condition_text = " AND ".join([f"{variable}={term}" for variable, term in conditions.items()])

        print(f"\nR{i + 1}: IF {condition_text} THEN Output={output_term}")
        print(f"Firing strength = min({', '.join(map(str, values))}) = {firing_strength}")
        print(f"Output membership = {modified_output}")

    return rule_outputs, firing_strengths

def aggregate_outputs(rule_outputs):
    if len(rule_outputs) == 0:
        return []

    aggregated = []
    for i in range(len(rule_outputs[0])):
        maximum = 0
        for rule_output in rule_outputs:
            if rule_output[i] > maximum:
                maximum = rule_output[i]
        aggregated.append(maximum)

    return aggregated

def defuzzify(uod, aggregated):
    numerator = 0
    denominator = 0
    for i in range(len(uod)):
        numerator += uod[i] * aggregated[i]
        denominator += aggregated[i]
    if denominator == 0:
        return 0
    return numerator/denominator


def display_fuzzification(memberships):
    print("\nFUZZIFICATION")
    for var, terms in memberships.items():
        print(f"\n{var}:")
        for term, value in terms.items():
            print(f"  {term} = {value}")


def run_fuzzy_system():
    print("\nGENERIC MAMDANI FUZZY INFERENCE SYSTEM")

    memberships = get_membership_values()
    output_name, universe, output_memberships = get_output_data()
    rules = get_rules()
    display_fuzzification(memberships)

    rule_outputs, firing_strengths = evaluate_rules(
        memberships,
        rules,
        universe,
        output_memberships
    )

    print("\nIMPLICATION / OUTPUT OF EACH RULE")
    for i in range(len(rule_outputs)):
        print(f"R{i + 1}: {rule_outputs[i]}")
    aggregated = aggregate_outputs(rule_outputs)

    print("\nAGGREGATION")
    print("Output universe:")
    print(universe)
    print("Aggregated membership values:")
    print(aggregated)
    crisp_value = defuzzify(universe, aggregated)

    print("\nDEFUZZIFICATION")
    print("Numerator:")
    numerator = sum(universe[i] * aggregated[i] for i in range(len(universe)))
    print(f"Sigma(Y_i × mu(Y_i)) = {numerator}")
    denominator = sum(aggregated)
    print("Denominator:")
    print(f"sigma(mu(Y_i)) = {denominator}")

    if denominator != 0:
        print(f"\nCrisp {output_name} = {numerator} / {denominator}")
        print(f"Final {output_name} = {crisp_value:.2f}")
    else:
        print("\nCrisp output cannot be calculated because")
        print("the total membership value is zero")


def main():
    while True:
        print("1. Run Mamdani Fuzzy Inference System")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            run_fuzzy_system()
        elif choice == "2":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")

main()