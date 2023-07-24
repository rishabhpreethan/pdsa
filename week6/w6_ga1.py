# Let L be a list with k elements where each element is a sorted list of integers. write a function 
# mergeKLists(L) that merges all the lists into a single sorted list and returns it. Try to write a solution 
# that runs in O(nlogk) time complexity, where n is the total number of integers in all k lists combined

# Input
# 2
# 4 5
# 8 26 69

# output
# 4 5 8 26 69


import heapq

def mergeKLists(L):
    min_heap = []
    for i, lst in enumerate(L):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
            
    result = []
    while min_heap:
        val, list_index, index_in_list = heapq.heappop(min_heap)
        result.append(val)
        index_in_list += 1
        if index_in_list < len(L[list_index]):
            heapq.heappush(min_heap, (L[list_index][index_in_list], list_index, index_in_list))
    
    return result
k = int(input())
LL=[]
for i in range(k):
    subL = [int(item) for item in input().split(" ")]
    LL.append(subL)
print(*mergeKLists(LL))