""" 
    Computes the shortest's paths between nodes of an undirected weighted graph
"""

import sys
from heapq import heappush, heappop
import pdb


def main():
    """ Main function """

    if len(sys.argv) != 3:
        print("Usage: python dijkstra.py <file-path>",
              "<destination-vertexes-string>")

    filepath = sys.argv[1]
    graph = read_graph(filepath)

    destinations = [int(x) for x in sys.argv[2].strip().split(',')]

    distances = []
    for destination in destinations:
        distance, _ = shortest_path(graph, 1, destination)
        distances.append(distance)

    print(*distances, sep=',')


def shortest_path(graph, init_v, end_v):
    """ Computes the shortest's path with the Dijkstra's algorithm """
    heap = []
    current_node = init_v
    current_length = 0

    while True:
        for edge in graph[current_node]:

            edge = (current_length + edge[0], edge[1])

            # check if it is already in the heap
            previous_distance = [item for item in heap if item[1] == edge[1]]

            if len(previous_distance) != 0 and previous_distance[0][0] < edge[0]:
                edge = previous_distance[0]
                heap.remove(previous_distance[0])

            heappush(heap, edge)
            
        current_length, current_node = heappop(heap)

        if current_node == end_v:
            break

    return current_length, []


def read_graph(filepath):
    """ Function for loading a graph """ 

    graph = {}
    
    for line in open(filepath):
        node_info = line.strip().split('\t')

        node = int(node_info[0])
        edges = node_info[1:]

        graph[node] = []

        for edge in edges:
            destination, weight = tuple([int(x) for x in edge.strip().split(',')])
            graph[node].append((weight, destination))

    return graph


if __name__ == '__main__':
    # pdb.run('main()')
    main()
