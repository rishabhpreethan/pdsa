# Write a function min_cost_walk(WList,S,D,V) that accepts a weighted adjacency list WList for an undirected and connected graph. The function returns the minimum cost and walk route in the format (minimum_cost, [walk_route]) from node S to node D, via node V (S -> V -> D), where the cost of a walk is the sum of weights of edges encountered on the route
# Note: Node can be repeated in the path

# input : 
# 7
# [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
# 0
# 4
# 5
# output
# (198, [0,1,2,5,6,4])


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