"""
    This script computes the Karger Min Cut algorithm, running n^3 times
"""

import sys
import random
import copy

def main():
    """Main function"""

    min_cut = sys.maxsize 

    original_graph = {line.strip().split('\t')[0]: line.strip().split('\t')[1:] 
                      for line in open('kargerMinCut.txt')}

    tries = len(original_graph) ** 1
    
    for _ in range(tries):
        graph = copy.deepcopy(original_graph)

        while len(graph) > 2:

            rand_v = random.sample(list(graph), 1)[0]
            rand_e = random.sample(graph[rand_v], 1)[0]

            # delete (future) self edge
            graph[rand_e] = list(filter(rand_v.__ne__, graph[rand_e]))
            graph[rand_v] = list(filter(rand_e.__ne__, graph[rand_v])) 

            # merge both lists of edges
            graph[rand_v] = graph[rand_v] + graph[rand_e] 

            # change vertex end in edges ending in 'rand_e'
            for vertex in graph[rand_e]:
                graph[vertex] = [val if val != rand_e else rand_v for val in graph[vertex]]

            # finally remove 'rand_e' vertex
            del graph[rand_e]
            
        min_cut = min(min_cut, len(list(graph.values())[0]))

    print(min_cut)


if __name__ == "__main__":
    main()
