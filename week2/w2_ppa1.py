# write a python function binarySearchIndexAndComparisons(l,k) 
# that accepts a list l sorted in ascending order and an integer k and 
# returns a tuple (True/False, numComparisons). the first part of this tuple 
# will be True if integer k is present in list l, false otherwise. the second 
# part of the tuple is an integer which gives the number of elements in l that
# are actually compared to k while searching k in the list l using binary search

def binarySearchIndexAndComparisons(l, k):
    low = 0
    high = len(l) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if l[mid] == k:
            return (True, comparisons)
        elif l[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return (False, comparisons)