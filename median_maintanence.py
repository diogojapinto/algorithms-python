"""
    Script with the Median Maintanence algorithm using an heap
"""

from sys import argv
from heapq import heappush, heappop


def main():
    """ Main function """
    filepath = argv[1]

    lower_heap = []
    higher_heap = []
    accumulator = 0

    for line in open(filepath):
        value = int(line.strip())

        if len(lower_heap) == 0 or value < -lower_heap[0]:
            heappush(lower_heap, -value)
        else:
            heappush(higher_heap, value)

        while len(higher_heap) > len(lower_heap):
            value = heappop(higher_heap)
            heappush(lower_heap, -value)

        while len(lower_heap) > len(higher_heap) + 1:
            value = heappop(lower_heap)
            heappush(higher_heap, -value)

        accumulator += -lower_heap[0]

    accumulator %= 10000
    print(accumulator)



if __name__ == '__main__':
    main()
