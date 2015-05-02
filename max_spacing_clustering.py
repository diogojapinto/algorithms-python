""" 
    Computes the max-spacing k-clustering of a graph
"""
import sys
from heapq import heappop, heapify

def main():
    """ Main function """

    # initialization
    nr_clusters = int(sys.argv[1])
    nodes, graph = build_graph()
    spacing = 0
    clusters = [set([x]) for x in nodes]

    # orders the edges by cost
    heapify(graph)

    while len(clusters) >= nr_clusters:
        cost, node1, node2 = heappop(graph)

        # retrieve the clusters to be merged
        cluster1 = None
        cluster2 = None

        for cluster in clusters:
            if node1 in cluster:
                cluster1 = cluster
            if node2 in cluster:
                cluster2 = cluster

        if cluster1 == cluster2:
            continue

        cluster1 |= cluster2
        clusters.remove(cluster2)

        if len(clusters) < nr_clusters:
            spacing = cost

    print(spacing)


def build_graph():
    """ Returns the graph corresponding to the file 'edges.txt' """

    graph = []
    nodes = set()

    for line in open('clustering1.txt'):
        elems = [int(x) for x in line.strip().split()]

        if len(elems) != 1:
            node1, node2, cost = elems
            nodes.add(node1)
            nodes.add(node2)
            graph.append((cost, node1, node2))

    return nodes, graph


if __name__ == '__main__':
    main()
