"""
    Computes a special max-spacing k-clustering
"""

from heapq import heappop, heapify
from operator import itemgetter

def main():
    """ Main function """

    initial_clusters = aggregate_vertices()
    edges_groups = formulate_edges(initial_clusters)

    accum = 0

    for edges in edges_groups:
        heapify(edges)
        clusters = [set(x) for x in map(itemgetter(1, 2), edges)]

        while len(edges):
            print(len(edges))
            _, node1, node2 = heappop(edges)

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
        accum += len(clusters)

    print(accum)



def aggregate_vertices():
    """ Aggregate elements by sumation """

    initial_clustering = {}
    # counter = 0
    for line in open('clustering_big.txt'):
        elem = [int(x) for x in line.strip().split()]
        if len(elem) == 2:
            continue
        sumation = sum(elem)
        initial_clustering.setdefault(sumation, [])
        initial_clustering[sumation].append(elem)

        #counter += 1
        #if counter == 10000:
        #    break

    return initial_clustering

def elems_distance(elem1, elem2):
    """ Computes the distance between elements """
    accum = 0
    for i in range(len(elem1)):
        if elem1[i] != elem2[i]:
            accum += 1
    return accum


def formulate_edges(clusters):
    """ Computes the edges comming from the minimization step """

    edges = []
    for original_index in sorted(clusters.keys()):
        inside_edges = []

        dest_list = clusters[original_index]

        if original_index + 1 in clusters.keys():
            dest_list.extend(clusters[original_index + 1])
        if original_index + 2 in clusters.keys():
            dest_list.extend(clusters[original_index + 2])

        for node1 in clusters[original_index]:
            for node2 in dest_list:
                distance = elems_distance(node1, node2)
                inside_edges.append((distance, node1, node2))

        print()
        edges.append(inside_edges)

    return edges


if __name__ == '__main__':
    main()
