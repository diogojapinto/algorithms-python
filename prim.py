""" 
    Computes the minimum-spanning tree using Prim's algorithm
"""
import sys
from heapq import heappush, heappop, heapify

def main():
    """ Main function """

    graph = build_graph()

    min_span_tree = {}
    vertices_costs = []

    # add all edges to the heap
    for i in graph.keys():
        vertices_costs.append((sys.maxsize, i))

    cost_accum = 0

    previous_vertex = None

    while len(min_span_tree) != len(graph):
        cost, vertex = heappop(vertices_costs)

        if vertex in min_span_tree:
            continue

        # if it is not the initial node
        if cost != sys.maxsize:
            cost_accum += cost

        # add the vertex to the minimum spanning tree
        if previous_vertex != None:
            min_span_tree.setdefault(previous_vertex, [])
            min_span_tree.setdefault(vertex, [])
            min_span_tree[previous_vertex].append(vertex)
            min_span_tree[vertex].append(previous_vertex)
        
        previous_vertex = vertex

        # add the accessible vertices to the heap
        for edge, length in graph[vertex]:
            heappush(vertices_costs, (length, edge))

    print(cost_accum)





def build_graph():
    """ Returns the graph corresponding to the file 'edges.txt' """

    graph = {}

    for line in open('edges.txt'):
        elems = [int(x) for x in line.strip().split()]

        if len(elems) != 2:
            node1, node2, cost = elems

            graph.setdefault(node1, [])
            graph.setdefault(node2, [])
            graph[node1].append([node2, cost])
            graph[node2].append([node1, cost])

    return graph


if __name__ == '__main__':
    main()
