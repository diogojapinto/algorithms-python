""" 
    Computes the 2-SAT problem, using Local Search algorithm 
"""

import sys

def main():
    """ Main function here """

    # Parse file
    in_file = open(sys.argv[1])
    nr_variables = int(in_file.strip())

    clauses = []

    for line in in_file:
        var1, var2 = [int(x) for x in line.strip().split()]
        clauses.append((var1, var2))

    



if __name__ == '__main__':
    main()
