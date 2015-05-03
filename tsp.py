"""
    Solves the Traveling Salesman Problem using dynamic programming
"""

from itertools import combinations
from math import sqrt
import matplotlib.pyplot as plt

INFINITY = float('inf')

#@profile
def main():
    """ Main function here """

    # Parse the file
    in_file = open('tsp2.txt')
    _ = int(in_file.readline().strip()) # nr_cities

    cities = []

    for line in in_file:
        x_coord, y_coord = [float(x) for x in line.strip().split()]
        cities.append((x_coord, y_coord))

    starting_point = (0, cities[0])

    distances = precompute_distances(cities)

    #plt.plot([x[0] for x in cities], [x[1] for x in cities], 'ro')
    #plt.show()
    #return

    # main loop
    solutions = {}
    solutions[frozenset([starting_point])] = [INFINITY] * len(cities)
    solutions[frozenset([starting_point])][0] = 0
    for nr_elems in range(1, len(cities)):
        new_solutions = {}

        for vertex_set in get_ordered_subsets(cities[1:], nr_elems):
            vertex_set = vertex_set.union({starting_point})
            new_solutions[vertex_set] = [INFINITY] * len(cities)

            for j, vertex1 in vertex_set:
                if j == 0:
                    continue

                min_solution = INFINITY
                old_set = vertex_set.difference({(j, vertex1)})

                for k, vertex2 in vertex_set:
                    if j == k:
                        continue
                    min_solution = min(min_solution,
                                       solutions[old_set][k] + 
                                       distances[vertex1][vertex2])

                new_solutions[vertex_set][j] = min_solution

        solutions = new_solutions

    min_solution = INFINITY
    for key in solutions:
        if len(key) != len(cities):
            continue

        for j, value in enumerate(solutions[key]):
            new_solution = value + euclidian_distance(cities[j], starting_point[1])
            min_solution = min(min_solution, new_solution)

    print(min_solution)


def get_ordered_subsets(lst, nr_elems):
    """ Generator function that returns an cardinality-ordered permutation of the list """
    for combination in combinations(enumerate(lst, 1), nr_elems):
        yield frozenset(combination)

def euclidian_distance(point1, point2):
    """ Computes the euclidian distance (I know the name says everything, but 
        pylinter insists on asking for this comments, and as I know its for a
        good cause I do them anyway) """
    return sqrt((point2[0] - point1[0]) ** 2 +
                (point2[1] - point1[1]) ** 2)

def precompute_distances(points):
    """ Noneed to explain this either """

    distances = {}
    for point1 in points:
        distances[point1] = {}
        for point2 in points:
            distances[point1][point2] = euclidian_distance(point1, point2)

    return distances


if __name__ == '__main__':
    main()
