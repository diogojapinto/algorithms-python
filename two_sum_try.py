"""
    Script with the 2-SUM algorithm
"""

from sys import argv
import cProfile


def main():
    """ Main function """
    filepath = argv[1]

    print("Reading...")
    vals_list = [int(x) for x in open(filepath)]

    print("Converting...")
    min_abs_val = min([abs(x) for x in vals_list])
    hash_table = {get_key(x, min_abs_val): x for x in vals_list}


    counter = 0

    print("Processing...")

    possible_values = [hash_table.values]

    for total in range(-10000, 10001):
        for key1 in hash_table:
            parcel1 = hash_table[key1]
            parcel2 = total - parcel1

            if parcel1 == parcel2:
                continue

            key2 = get_key(parcel2, min_abs_val)
            if key2 in hash_table:
                counter += 1

    print(counter)


def get_key(value, min_value):
    """ Produces a key based on the value, by subtracting to the absolute value 
    the minimum absolute value in the dataset """
    if value < 0:
        signal = -1
    else:
        signal = 1

    return (abs(value) - min_value) * signal


if __name__ == '__main__':
    #main()
    cProfile.run('main()')
