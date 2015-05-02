""" 
    Computes the greedy allocation of jobs
    The first options uses difference (weight - length), the second one the ration (weight/length)
"""

def main():
    """ Main function here """

    jobs = [line.strip().split() for line in open('jobs.txt')]
    jobs = [[int(x[0]), int(x[1])] for x in jobs]

    jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    jobs = sorted(jobs, key=ratio, reverse=True)

    weighted_sum = 0
    length_sum = 0

    for job in jobs:
        length_sum += job[1]
        weighted_sum += length_sum * job[0]

    print(weighted_sum)

def difference(job):
    """ Computes the difference measure for a job """
    return job[0] - job[1]

def ratio(job):
    """ Computes the ratio measure for a job """
    return job[0] / job[1]


if __name__ == '__main__':
    main()
