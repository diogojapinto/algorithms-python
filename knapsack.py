""" 
	Solves the Knapsack problem
"""

def main():
    """ Main function """

    # Retrieves the items
    items = []
    f_input = open('knapsack_big.txt')

    knapsack_size, _ = [int(x) for x in f_input.readline().strip().split()]

    for line in f_input:
        value, weight = [int(x) for x in line.strip().split()]
        items.append((weight, value))

    # items = sorted(items)

    # Now for the algorithm
    best_solutions = [0] * (knapsack_size + 1)

    for weight, value in items:
        new_solution = [0] * (knapsack_size + 1)
        for i in range(knapsack_size + 1):
            if weight <= i:
                new_value = best_solutions[i - weight] + value
                new_solution[i] = max(best_solutions[i], new_value)
            else:
                new_solution[i] = best_solutions[i]
        best_solutions = new_solution

    print(best_solutions[knapsack_size])

if __name__ == '__main__':
    main()
