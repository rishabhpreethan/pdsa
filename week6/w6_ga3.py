# Given an array based min heap arr write a function min_max(arr) that to convert arr to a max heap. 
# the function should change the original arr to amc heap. the expected time complexity is O(n)

# Input
# 66 55 43 34 12 7 2 20 5

# output
# True

def min_max(arr):
    n = len(arr)

    def heapify_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break

            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1

            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    for i in range(n // 2 - 1, -1, -1):
        heapify_down(i, n - 1)

arr = [3, 1, 4, 1, 5, 5, 3]
min_max(arr)