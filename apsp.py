"""
    Computes the All-Pairs-Shortest-Path algorithm (using Floyd-Warshall)
"""

import sys
import copy
import cProfile

def main(file):
    """ Main function """

    in_file = open(file)

    # Parse file
    nr_vertices, _ = [int(x) for x in in_file.readline().strip().split()]
    edges = []

    for line in in_file:
        node1, node2, length = [int(x) for x in line.strip().split()]
        edges.append((length, node1, node2))

    #Algorithm
    shortest_paths = [[sys.maxsize for x in range(nr_vertices)] for x in range(nr_vertices)]

    # initialization
    for length, node1, node2 in edges:
        shortest_paths[node1 - 1][node2 - 1] = length
    for i in range(nr_vertices):
        shortest_paths[i][i] = 0

    for k in range(nr_vertices):
        for i in range(nr_vertices):
            for j in range(nr_vertices):
                old_value = shortest_paths[i][j]
                new_value = min(
                    shortest_paths[i][k] + shortest_paths[k][j], 
                    sys.maxsize)

                shortest_paths[i][j] = min(old_value, new_value)

    # Detect negative cost cycle and remove the self edges from the equation
    for i in range(nr_vertices):
        if shortest_paths[i][i] < 0:
            print("NULL")
            return
        else:
            shortest_paths[i][i] = sys.maxsize



    print(min([min(x) for x in shortest_paths]))

if __name__ == '__main__':
    main("g1.txt")
    main("g2.txt")
    main("g3.txt")

