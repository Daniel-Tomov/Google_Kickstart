import statistics
import itertools

def sorted_k_partitions(seq, k):
    # absolute legend from https://stackoverflow.com/questions/39192777/how-to-split-a-list-into-n-groups-in-all-possible-combinations-of-group-length-a

    """Returns a list of all unique k-partitions of `seq`.

    Each partition is a list of parts, and each part is a tuple.

    The parts in each individual partition will be sorted in shortlex
    order (i.e., by length first, then lexicographically).

    The overall list of partitions will then be sorted by the length
    of their first part, the length of their second part, ...,
    the length of their last part, and then lexicographically.
    """
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    # Sort the parts in each partition in shortlex order
    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    # Sort partitions by the length of each part, then lexicographically.
    result = sorted(result, key = lambda ps: (*map(len, ps), ps))

    return result

def permutations(arr): return list(itertools.permutations(arr, len(arr)))

def median(arr): return float(statistics.median(arr))

def minDiff(arr, n):
    # Initialize difference as infinite
    diff = 10**20
    a = 0
    b = 0

    # Find the min diff by comparing difference
    # of all possible pairs in given array
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(arr[i]-arr[j]) < diff:
                diff = abs(arr[i] - arr[j])
                a = arr[i]
                b = arr[j]
 
    # Return min diff
    return a, b, diff

def main():
    #inputs = open("image_labeler_sample_ts2_input.txt", 'r').readlines()
    testCases = int(input())
    for cases in range(0, testCases):
        lineTwo = input().split(" ")
        countries = int(lineTwo[0])
        categories = int(lineTwo[1])
        people = [int(x) for x in input().split(' ')]
        people.sort()


        #print(testCases)
        #print(countries)
        #print(categories)
        #print(people)
        if categories == 1:
            print(f'Case #1: {median(people)}')
        else:
            medians = []
            partitions = sorted_k_partitions(people, categories)
            for i in partitions:
                med = 0
                for n in i:
                    med = med + median(n)
                medians.append(med)
            print(f'Case #{testCases}: {float(max(medians))}')
       
        

        

if __name__ == "__main__":
    main()