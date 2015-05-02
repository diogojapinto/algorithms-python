"""
    Script with the 2-SUM algorithm
"""

from sys import argv
import cProfile


def main():
    """ Main function """
    filepath = argv[1]

    print("Reading...")
    hash_table = set([int(x) for x in open(filepath)])
    counter = 0

    print("Processing...")
    for total in range(-10000, 10001):
        for parcel1 in hash_table:
            parcel2 = total - parcel1
            if parcel2 != parcel1 and parcel2 in hash_table:
                counter += 1
                break

    print(counter)



if __name__ == '__main__':
    #main()
    cProfile.run('main()')
