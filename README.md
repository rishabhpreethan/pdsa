# NOTES

## WEEK 3
### Quicksort (Divide and conquer)
* Choose a pivot element (Typically the first element)
* Partition L into lower and upper parts with respect to the pivot
* Move the pivot between the lower and upper partition
* Recursively sort the two partitions
    * Partitioning
        * Scan list from left to right
        * Four segments: pivot, lower, upper, unclassified
            * Examine the first unclassified element
            * If > pivot, extend upper to include this element
            * If <= pivot, exchange with the first element in upper. This extends lower and shifts upper by one position.
#### Time
* `O(nlogn)`
* `Worst case` : `O(n^2)`  (Already sorted)

```python
def quicksort(L,l,r):
    if (r - l <= 1):
        return (L)
    (pivot, lower, upper) = (L[l], l+1, l+1)

    for i in range(l+1, r):
        if L[i] > pivot:        # Extend upper segment
            upper += 1
        else:                   # Exchange L[i] with the start of upper segment
            (L[i], L[lower]) = (L[lower], L[i])
            (lower, upper) = (lower+1, upper+1)    # Shift both segments

    # Move pivot between lower and upper
    (L[l], L[lower-1]) = (L[lower-1], L[l])

    lower-=1

    quicksort(L, l, lower)
    quicksort(L, lower+1, upper)
    
    return (L)
```

### Lists (Linked lists)
* Flexible length
* Easy to modify the structure
* Values are scattered in memory
```python
class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return
    
    def isempty(self):
        if self.value == None:
            return (True)
        else:
            return (False)

    #RECURSIVE
    def append(self, v):
        if self.isempty():
            slef.value = v
        elif self.next == None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return

    #ITERATIVE
    def append(self, v):
        if self.isempty():
            self.value = v
            return 
        
        temp = self
        while temp.next != None:
            temp = temp.next

        temp.next = Node(v)
        return
    
    def insert(self, v):
        if self.isempt():
            self.value = v
            return
        
        newnode = Node(v)

        #Exchange value in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)

        #Switch links
        (self.next, newnode.next) = (newnode, self.next)
        return

    def delete(self, v):
        if self.isempty():
            return
        
        if slef.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return
```

### Arrays
* Fixed size
* Supports random access
* Allocate a contiguous block of memory
