""" 
    Computes the 2-SAT problem, using Local Search algorithm 
"""

import sys
import math
import random

def main(filename):
    """ Main function here """

    # Parse file
    in_file = open(filename)
    nr_variables = int(in_file.readline().strip())

    clauses = []

    for line in in_file:
        var1, var2 = [int(x) for x in line.strip().split()]
        clauses.append((var1, var2))

    for _ in range(math.floor(math.log(nr_variables, 2))):
        #variables = [random.choice([False, True]) for _ in range(nr_variables)]
        variables = init_variables(clauses, nr_variables)
        for _ in range(2 * nr_variables ** 2):
            valid, clause_nr = verify_satisfiability(variables, clauses)
            if valid:
                print("True")
                return
            else:
                pivot = random.randint(0, 1)
                var_i = abs(clauses[clause_nr][pivot]) - 1
                variables[var_i] = not variables[var_i]

    print(False)

def init_variables(clauses, nr_variables):
    """ Initializes the variables approximately to the clauses """

    random.shuffle(clauses)
    variables = [random.choice([False, True]) for _ in range(nr_variables)]

    for clause in clauses:
        var1 = abs(clause[0]) - 1
        var2 = abs(clause[1]) - 1
        truth1 = clause[0] >= 0
        truth2 = clause[1] >= 0

        variables[var1] = truth1
        variables[var2] = truth2

    return variables



def verify_satisfiability(variables, clauses):
    """ Do I really need to explain this? """
    
    for i, clause in enumerate(clauses):
        var1 = abs(clause[0]) - 1
        var2 = abs(clause[1]) - 1
        truth1 = clause[0] >= 0
        truth2 = clause[1] >= 0

        if not (variables[var1] == truth1 or variables[var2] == truth2):
            return False, i

    return True, None


if __name__ == '__main__':
    #main("2sat1.txt")
    #main("2sat2.txt")
    #main("2sat3.txt")
    #main("2sat4.txt")
    #main("2sat5.txt")
    #main("2sat6.txt")
    main("2sat.txt")
