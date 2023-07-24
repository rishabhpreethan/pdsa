# NOTES


## WEEK 2
### Calculating Complexities
```python
def noDup(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            if L[i] == L[j]:
                return False
    return True

# Time complexity
O(n²)
```
```python
def matrixmult(a,b):
    (m,n,p) = (len(a), len(b), len(b[0]))

    c = [[0 for i in range(p) ]
            for j in range(m) ]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] = c[i][j] + A[i][k] * B[k][j]
    return c

# Time complexity
O(n³)
```
```python
def numberofnits(n):
    count = 1
    while n > 1:
        count += 1
        n = n // 2
    return count

# Time complexity
O(logn)
```

### Searching
#### Linear Search
```python
def linearsearch(v, l):
    for x in l:
        if v == x:
            return True
    return False

# Time complexity
O(n) - worst case
```

#### Binary Search
```python
def binarysearch(v, l):
    if l == []:
        return False
    m = len(l) // 2

    if v == l[m]:
        return m
    if v < l[m]:
        return binarysearch(v, l[:m])
    else:
        return binarysearch(v, l[m+1:])

# Time complexity
O(logn)
```

### Sorting
#### Selection Sort
* Select the next element in sorted order
* Append it to the final sorted list
* Avoid using a second list
    * Swap the minimum element into the first position
    * Swap the second minimum element into the second position
* Eventually the list is rearranged in place in ascending order
```python
def SelectionSort(l):
    n = len(l)
    if n < l:
        return l

    for i in raneg(n):
        mpos = i
        for j in range(i+1, n):
            if l[j] < l[mpos]:
                mpos = j
        # l[mpos] : smallest value in l[i:]
        l[i], l[mpos] = l[mpos], l[i]
        # Now l[:i+1] is sorted
    return l

# Time complexity
O(n²)
```

#### Insertion Sort
* Start building a new sorted list
* Pick next element and insert it into the sorted list
* An iterative formulation
    * Assume ```l[:i]``` is sorted
    * Insert ```l[i]``` in ```l[:i]```
* A recursive formulation
    * Inductively sort ```l[:i]```
    * Insert ```l[i]``` in ```l[:i]```
```python
# ITERATIVE
def insertionsort(l):
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        j = i
        while(j>0 and l[j] < l[j-1]):
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l

# Time complexity
O(n²)


# RECURSIVE
def insert(l, v):
    n = len(l)
    if n == 0:
        return [v]
    if v >= l[-1]:
        return l + [v]
    else:
        return insert(l[:-1], v) + l[-1:]

def isort(l):
    n = len(n)
    if n < l:
        return l
    l = insert(isort(l[:-1]), l[-1])
    return l

# Time complexity
O(n²) - worst case
O(n)  - best case
```

#### Merge Sort
* Combine two sorted lists a and b into a single sorted list c
    * Compare first elements of a and b
    * Move the smaller of the two to c
    * Repeat till you exhaust a and b
* Merging a and b
    * let n be the length of l
    * sort a[:n//2]
    * sort a[n//2:]
    * merge the sorted halves into b
```python
def merge(a, b):
    m, n = len(a), len(b)
    c, i, j, k = [], 0, 0, 0

    while k < m+n:
        if 1 == m:
            c.extend(b[j:])
            k = k + (n-j)
        elif j == n:
            c.extend(a[i:])
            k = k + (n-1)
        elif a[i] < b[j]:
            c.append(b[j])
            i, k = (i+1, k+1)
        else:
            c.append(b[j])
            j, k = j+1, k+1
    return c

# Time complexity
O(n logn)
```

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
<br>

### Implementing a dictionary
* The underlying storage is an array
    * Given an offset 9, find a[i] in constant time
* Keys have to be mapped to {0,1,...n-1}
    * Given a key k, convert it to an offset i
* Hash Function
    * h:s -> x maps a set of values s to a small range of integers x = {0,1...,n-1}
    * Typically |x| << |s|, so there will be collisions, h(s) = h(s').s != s'
    * A good hash function will minimize collisions
    * SHA-256 is an industry standard hashing function whose range is 256 bits
        * Use to hash large files - avoid uploading duplicates to cloud storage


## WEEK 4
### Graphs G=(V,E)
* V is a set of vertices or nodes
* E is a set of edges
> A path is a squence of vertices v1,v2....vk connected by edges<br>
> Edges dont cross each other in a <b>planar graph</b><br>
> Independent set - subset of vertices such that no two are connected by an edge
<br>


#### Directed Graph
* (v, v') ∈ E does not imply (v', v) ∈ E
<br>


#### Undirected graph
* (v, v') ∈ E if (v', v) ∈ E
* (v, v'), (v', v) are the same edge

#### Adjacency matrix
* If a path exists it is labelled as 1
```python
import numpy as np
a = np.zeros(shape = (10, 10))

for (i, j) in edges:
    a[i, j] = 1
```
> Symmetry across main diagonal for an undirected graph

|      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|---|
| 0    | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1    | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2    | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3    | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 4    | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 5    | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 6    | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| 7    | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 8    | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| 9    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

<br>

#### Neighbours of i - column j with entry 1
* Neighbours of 4 are [0, 3, 7] (above diagram)
```python
def neighbours(mat, i):
    d = []
    (rows, cols) = mat.shape
    for j in range(cols):
        if mat[i, j] == 1:
            d.append(j)
    return d

neighboours(mat, 8)

O/P:
[5, 9]
```
<br>

#### Degree of a vertex i
* Undirected graphs
    * degree(6) = 1
* Directed graphs
    * indegree(6) = 1
    * degree(6) = 1
    > used a undirected graph in the example, values could be different
<br>


#### Adjacency list
|       | Connected to |
|-------|--------------|
| 0 |    [1, 4]    |
| 1 |    [2]    |
| 2 |    [0]    |
| 3 |    [4, 6]    |
| 4 |    [0, 3, 7]    |
| 5 |    [3, 7]    |
| 6 |    [5]    |
| 7 |    [4]    |
| 8 |    [5, 9]    |
| 9 |    [8]    |
```python
def adjacency():
    adlist = {}
    for i in range(10):
        adlist[i] = []
        for (i, j) in edges:
            adlist[i].append(j)
    return adlist
```
  
<br>

 
### BFS (breadth first search)
* Explore the graph level by level
* Each visited vertex has to be explored
* Maintain information about the vertices
> O(n²)    - adjacency matrix<br>
> O(V + E) - adjacency list

#### Steps
##### Maintain a sequence of visited vertices yet to be explored
* A queue - first in, first out
* Initially empty
```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def addq(self, v):
        self.queue.append(v)
    
    def delq(self):
        v = None
        if not self.isempty():
            v.self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def isempty(self):
        return self.queue == []
    
    def __str__(self):
        return str(self.queue)

    # BFS Function
    def BFS(mat, v):
        (rows, cols) = mat.shape
        visited = {}
        for i in range(rows):
            visited[i] = False
        q = Queue()

        visited[v] = True
        q.addq(v)

        while(not q.isempty()):
            j = q.delq()
            for k in neighbours(mat, j):
                if(not visited[k]):
                    visited[k] = True
                    q.addq(k)
        return visited

    # BFS List Path
    def BFSListPath(mat, v):
        (visited, parent) = ({}, {})
        for i in mat.keys():
            visited[i] = False
            parent[i] = -1
        q = Queue()

        visited[v] = True
        q.addq(v)

        while(not q.isempty()):
            j = qdelq()
            for k in mat[j]:
                if not visited[k]:
                    visited[k] = True
                    parent[k] = j
                    q.addq(k)
        return (visited, parent)

    # BFS to record distance
    def BFSListPathLevel(mat, v):
        (level, parent) = ({}, {})
        for i in mat.keys():
            level[i] = -1
            parent[i] = -1
        q = Queue()

        level[v] = 0
        q.addq(v)

        while(not q.isempty()):
            j = q.delq()
            for k in mat[j]:
                if level[k] == -1:
                    level[k] = level[j] + 1
                    parent[k] = j
                    q.addq(k)
        return (level, parent)
```
<br>


### DFS (Depth First Search) - O(V + E)
```python
def DFSInit(mat):
    (rows, cols) = mat.shape
    (visited, parent) = ({}, {})
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return (visited, parent)
    
def DFS(mat, visited, parent, v):
    visited[v] = True

    for k in neighbours(mat, v):
        if not visited[k]:
            parent[k] = v
            (visited, parent) = DFS(mat, visited, parent, k)
    return (visited, parent)

# Global
# A mutable value can be globally referenced from inside a function
(visited, parent) = ({}, {})

def DFSInitGlobal(mat):
    (rows, cols) = mat.shape
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return

def DFSGlobal(mat, v):
    visited[v] = True
    
    for k in neighbours(mat, v):
        if not visited[k]:
            parent[k] = v
            DFSGlobal(mat, k)
    return
```
```python
# Using an adjacency list
def DFSInitList(lis):
    (visited, parent) = ({}, {})
    for i in lis.keys():
        visited[i] = False
        parent[i] = -1
    return (visited, parent)

def DFSList(lis, visited, parent, v):
    visited[v] = True

    for j in lis[k]:
        if not visited[k]:
            parent[k] = v
            (visited, parent) = DFSList(lis, visited, parent, k)
    return (visited, parent)


# Global
(visited, parent) = ({}, {})

def DFSInitListGlobal(lis):
    for i in lis.keys():
        visited[i] = False
        parent[i] = -1
    return

def DFSListGlobal(lis, v):
    visited[v] = True

    for k in lis[v]:
        if not visited[k]:
            parent[k] = v
            DFSListGlobal(lis, k)
    return
```
<br>


### Topological Sorting
```Every DAG can be topologically sorted```<br>
```Every DAG has a vertex with indegree 0```

* A graph with directed cycles cannot be sorted topologically
* Path i -> j means i must be listed before j
```python
# Using ADJACENCY MATRIX
def toposort(mat):
    rows, cols = mat.shape
    indegree = {}
    toposortlist = []

    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if mat[r,c] == 1:
                indegree[c] = indegree[c] + 1
    for i in range(rows):
        j = min([k for k in range(cols)
                   if indegree[k] == 0 ])
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in range(cols):
            if mat[j, k] == 1:
                indegree[k] = indegree[k] - 1
    return toposortlist

# Time complexity
O(n²)
```
```python
# Using ADJACENCY LIST
def toposortlist(l):
    indegree = {}
    toposortlist = []
    for u in l.keys():
        for v in l[u]:
            indegree[v] = indegree[v] + 1
    
    zerodegreeq = Queue()
    for u in l.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)
    
    while (not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in l[j]:
            indegree[k] = indegree[k] - 1
            if indegree[k] == o:
                zerodegree.addq(k)
    return toposortlist

# Time complexity
O(m + n)
```

## WEEK 5
### Dijkstra's Algorithm
* Greedy algorithm
* No negative edges
```python
# Using ADJACENCY MATRIX
def dijkstras(mat, s):
    rows, cols, x = mat.shape
    infinity = np.max(mat) + rows + 1
    visited, distance = ({}, {})
    for v in range(rows):
        visited[v], distance[v] = False, infinity
    distance[a] = 0
    for u in range(rows):
        nextd = min(distance[v] for v in range(rows)
                        if no visited[v])
        nextvlist = [v for v in range(rows)
                        if not visited[v] and
                        distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for v in range(cols):
            if mat[nextv, v, 0] == 1 and (not visited[v]):
                distance[v] = min(distance[v], distance[nextv] + mat[nextv ,v, 1])
    return distance



# Using ADJACENCY LIST
def dijkstralist(l, s):
    infinity = 1 + len(l.keys()) * max([d for u in l.keys()
                                            for (v, d) in l[u]])
    visited, distance = ({}, {})
    for v in l.keys():
        visited[v], distance[v] = (False, infinity)
    distance[s] = 0
    for u in l.keys():
        nextd = min([distance[v] for v in l.keys()
                        if not visited[v]])
        nextvlist = [v for v in l.keys()
                        if not visited[v] and
                        distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for (v, d) in l[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v], distance[nextv])
    return distance

# Time complexity
O(n²)   # for both
```

### Bellman-Ford Algorithm
* No cycles