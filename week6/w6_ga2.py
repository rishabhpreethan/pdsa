# Write a Python function maxLessThan(root, K), that accepts the root node of the binary search tree 
# and a number K and returns the maximum number less than or equal to K in the tree. If K is the less 
# than every number in the tree return None . Each node in the tree is an object of class Tree , and the 
# tree will have at least one node.

# Input
# 23235 82107 35775 91961 4323 40556 76603 64302 27316 74372
# 2000

# output
# None


def min_cost_walk(WList, S, D, V):
    def bellman_ford(graph, start):
        n = len(graph)
        distances = [float('inf')] * n
        distances[start] = 0
        path = [-1] * n

        for _ in range(n - 1):
            for u in range(n):
                for v, cost in graph[u]:
                    if distances[u] + cost < distances[v]:
                        distances[v] = distances[u] + cost
                        path[v] = u

        return distances, path

    distances_s, path_s = bellman_ford(WList, S)
    distances_v, path_v = bellman_ford(WList, V)

    route_sv = []
    node = V
    while node != -1:
        route_sv.append(node)
        node = path_s[node]

    route_sv.reverse()

    route_vd = []
    node = D
    while node != -1:
        route_vd.append(node)
        node = path_v[node]

    route_vd.reverse()

    route = route_sv + route_vd[1:]
    total_cost = distances_s[V] + distances_v[D]

    return total_cost, route
size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))