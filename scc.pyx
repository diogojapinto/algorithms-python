"""
    This script computes the largest Strongly Connected Components from a directed graph
"""
from __future__ import print_function
import sys
import math
import cProfile

def main():
    """ Main function here"""

    print("Reading...")
    graph = read_graph()
    print("Inverting...")
    reversed_graph = reverse_graph(graph)

    # saves iteratively the finishing times, reversed
    finish_times = []
    explored_nodes = set()
    print("1st pass")
    for node in reversed_graph:
        if node not in explored_nodes:
            tmp = finish_times
            finish_times = dfs(reversed_graph, explored_nodes, node)
            finish_times += tmp

    # iterates through the lastly retrieved in the dfs call
    explored_nodes = set()
    clusters = []
    print("2nd pass")
    for node in finish_times:
        if node not in explored_nodes:
            clusters.append(dfs(graph, explored_nodes, node))

    clusters = sorted(clusters, key=len, reverse=True)

    print(*[len(x) for x in clusters[:5]], sep=',')
        

def dfs(graph, explored_nodes, node):
    """ Does a depth-first-search on a graph, returning the interesting 
    part for each iteration (1 or 2) """
    
    finish_times = []

    # starts-up the search stack
    stack = [node]

    # all_nodes = set(graph.keys())
    # for edges in graph.values():
    #     all_nodes = all_nodes.union(edges)

    # search loop
    while stack:
        # retrieves the next node to be searched
        node = stack.pop()

        # verify if it was already processed
        if node in explored_nodes:
            continue

        #sets the node as explored
        explored_nodes.add(node)

        # add it to the finish times
        finish_times.append(node)

        # adds edges to the stack
        new_nodes = [edge for edge in graph[node] if edge not in explored_nodes]
        stack += new_nodes


        # percentage = math.floor(len(explored_nodes) / len(all_nodes) * 100)

        # sys.stdout.write("\rCompletion: %d%%" % percentage)
        # sys.stdout.flush()

    # print()
    return finish_times



def read_graph():
    """ Parses a graph from a file, where in each line there is an edge in the form: 
    <source> <destination> """
    graph = {}
    # Build the graph
    for line in open("SCC.txt"):
        source, destination = [int(x) for x in line.strip().split()]
        if destination not in graph:
            graph[destination] = []
        if source in graph:
            graph[source].append(destination)
        else:
            graph[source] = [destination]

    return graph

def reverse_graph(graph):
    """ Reverses a graph's edges """
    reversed_graph = {}

    for node in graph:
        if node not in reversed_graph:
            reversed_graph[node] = []
        for edge in graph[node]:
            if edge in reversed_graph:
                reversed_graph[edge].append(node)
            else:
                reversed_graph[edge] = [node]

    return reversed_graph


if __name__ == '__main__':
    # cProfile.run('main()', 'out.txt', 'calls')
    main()
