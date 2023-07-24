# An internet service provider company wants to lay fiber lines to connect n cities labeled 0 to n-1. write a function FiberLink(distance_map) that accepts a weighted adjacency list distance_map in the following format:
# distance_map = {
# source_index : [(destination_index,distance(km)),(destination_index,distance),...]
# }

# input : 
# 7
# [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
# output
# 182



def find(parent, city):
    if parent[city] != city:
        parent[city] = find(parent, parent[city])
    return parent[city]

def union(parent, rank, city1, city2):
    root1 = find(parent, city1)
    root2 = find(parent, city2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def FiberLink(distance_map):
    edges = []
    for city, neighbors in distance_map.items():
        for neighbor, distance in neighbors:
            edges.append((distance, city, neighbor))

    edges.sort()
    num_cities = len(distance_map)
    parent = list(range(num_cities))
    rank = [0] * num_cities

    total_distance = 0
    for distance, city1, city2 in edges:
        if find(parent, city1) != find(parent, city2):
            union(parent, rank, city1, city2)
            total_distance += distance

    return total_distance
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))