"""
    Solves the Traveling Salesman Problem using dynamic programming
"""

from itertools import combinations
from math import sqrt

INFINITY = float('inf')

def main():
    """ Main function here """

    # Parse the file
    in_file = open('tsp.txt')
    _ = int(in_file.readline().strip()) # nr_cities

    cities = []

    for line in in_file:
        x_coord, y_coord = [float(x) for x in line.strip().split()]
        cities.append((x_coord, y_coord))

    starting_point = cities[0]

    # main loop
    solutions = {}
    solutions[frozenset(starting_point)] = [INFINITY] * len(cities)
    solutions[frozenset(starting_point)][0] = 0

    for vertex_set in get_ordered_subsets(cities[1:]):
        vertex_set = vertex_set.union({(0, starting_point)})
        solutions[vertex_set] = [INFINITY] * len(cities)

        for j, vertex1 in vertex_set:
            if vertex1 == starting_point:
                continue

            min_solution = INFINITY
            old_set = vertex_set.difference({(j, vertex1)})
            for k, vertex2 in vertex_set:
                if vertex1 == vertex2 or vertex2 == starting_point:
                    continue

                new_solution = solutions[old_set][k] + euclidian_distance(vertex1, vertex2)
                min_solution = min(min_solution, new_solution)

            solutions[vertex_set][j] = min_solution

    min_solution = INFINITY
    for j, value in enumerate(solutions[frozenset(cities)]):
        new_solution = value + euclidian_distance(cities[j], starting_point)
        min_solution = min(min_solution, new_solution)

    return min_solution


def get_ordered_subsets(lst):
    """ Generator function that returns an cardinality-ordered permutation of the list """
    for nr_elems in range(1, len(lst)):
        for combination in combinations(enumerate(lst, 1), nr_elems):
            yield frozenset(combination)

def euclidian_distance(point1, point2):
    """ Computes the euclidian distance (I know the name says everything, but 
        pylinter insists on asking for this comments, and as I know its for a
        good cause I do them anyway) """
    return sqrt((point2[0] - point1[0]) ** 2 +
                (point2[1] - point1[1]) ** 2)


if __name__ == '__main__':
    main()
