# write a function IsNegativeWeightCyclePresent(WList) that accepts a weighted adjacency 
# list Wlist for a directed and connected graph and returns True if the graph has a negative weight 
# cycle otherwise return false

# input:
# 4
# [(0,1,10),(0,2,-5),(0,3,2),(3,2,-5),(2,1,-2),(1,3,10)]

# output:
# False


def IsNegativeWeightCyclePresent(WList):
    def relax(u, v, weight, dist):
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            return True
        return False

    dist = {node: float('inf') for node in WList}
    dist[0] = 0

    for _ in range(len(WList) - 1):
        for u in WList:
            for v, weight in WList[u]:
                relax(u, v, weight, dist)

    for u in WList:
        for v, weight in WList[u]:
            if relax(u, v, weight, dist):
                return True

    return False
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))